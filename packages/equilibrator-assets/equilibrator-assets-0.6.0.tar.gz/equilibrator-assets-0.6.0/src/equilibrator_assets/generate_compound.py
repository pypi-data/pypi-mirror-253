# The MIT License (MIT)
#
# Copyright (c) 2013 The Weizmann Institute of Science.
# Copyright (c) 2018 Institute for Molecular Systems Biology, ETH Zurich.
# Copyright (c) 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""Create Compound objects outside of the compound-cache."""
import logging
from typing import List, NamedTuple, Optional

import pandas as pd
from equilibrator_api import ComponentContribution
from equilibrator_cache import Compound, CompoundCache, CompoundMicrospecies
from openbabel.pybel import readstring

from equilibrator_assets import chemaxon, group_decompose, molecule, thermodynamics


logger = logging.getLogger(__name__)
group_decomposer = group_decompose.GroupDecomposer()
cc = ComponentContribution()
TRAINING_IDS = cc.predictor.params.train_G.index


class GenerateCompoundResult(NamedTuple):
    """A result from one of the Compound generating functions."""

    structure: str
    compound: Optional[Compound]
    inchi_key: Optional[str]
    method: str
    status: str


def _populate_compound_information(row):
    """Attempt to populate a compound with key information.

    Accepts a pandas Series and attempts to generate a Compound.

    Returns a Compond or None if compound cannot be made.
    """
    if row.method == "chemaxon":
        # Use chemaxon to populate compound
        compound = Compound(**row.compound_dict)
        mol = molecule.Molecule.FromSmiles(compound.smiles)
    else:
        # Bypass chemaxon and use specified smiles
        compound_dictionary = {
            "atom_bag": chemaxon.get_atom_bag("smi", row.smiles),
            "dissociation_constants": [],
            "id": row.id,
            "smiles": row.smiles,
        }
        compound = Compound(**compound_dictionary)
        mol = molecule.Molecule.FromSmiles(row.smiles)

    if row.user_specified_pkas:
        # pkas in a string of form "A,B,C...""
        compound.dissociation_constants = [
            float(i) for i in row.user_specified_pkas.split(",")
        ]

    # Add extra information to compound
    compound.inchi_key = row.inchi_key
    try:
        decomposition = group_decomposer.Decompose(
            mol, ignore_protonations=False, raise_exception=True
        )
        compound.group_vector = decomposition.AsVector()
    except group_decompose.GroupDecompositionError:
        # Decomposition failed. If this is the first attempt
        # return None
        # If method is "empty" then store empty compound
        if row.method == "empty":
            compound.group_vector = None
        else:
            return None

    for ms_dict in thermodynamics.create_microspecies_mappings(compound):
        ms = CompoundMicrospecies(**ms_dict)
        compound.microspecies.append(ms)

    return compound


def create_compounds(
    mol_strings: List[str],
    mol_format: str = "smiles",
    bypass_chemaxon: bool = False,
    save_empty_compounds: bool = False,
    specified_pkas: dict = None,
) -> List[GenerateCompoundResult]:
    """Generate a Compound object directly from SMILESs or InChIs.

    Parameters
    ----------
    mol_strings : List[str]
        Structure of compounds to add (InChI or smiles)
    mol_format : str, optional
        The format the molecules are given in (smiles, inchi),
        by default "smiles"
    bypass_chemaxon : bool, optional
        Allows compounds that fail to be decomposed with chemaxon to be
        created with the user-specified structure instead, by default False
    save_empty_compounds : bool, optional
            Whether to insert compounds into the database that cannot be
            decomposed user-specified structure, by default False
    specified_pkas : dict, optional
            A dictionary of user-specified pkas of form
            {mol_string: [pka1, pka2], ...}
            where mol_string is found in mol_strings, by default dict()

    Returns
    -------
    List[GenerateCompoundResult]
        The created compounds
    """
    molecules = pd.DataFrame(
        data=[[-1 - i, s] for i, s in enumerate(mol_strings)],
        columns=[
            "id",
            "inchi",
        ],  # note that the "inchi" column can also contain SMILES strings
    )
    molecules["inchi_key"] = molecules.inchi.apply(
        lambda s: readstring(mol_format, s).write("inchikey").strip()
    )
    molecules["smiles"] = molecules.inchi.apply(
        lambda s: readstring(mol_format, s).write("smiles").strip()
    )
    molecules["compound_dict"] = list(
        thermodynamics.get_compound_mappings(
            molecules, "foo", num_acidic=20, num_basic=20
        )
    )
    # Specify dissociation constants if supplied
    molecules["user_specified_pkas"] = None
    if specified_pkas:
        for species, species_pkas in specified_pkas.items():
            if molecules["inchi"].str.contains(species, regex=False).any():
                molecules.loc[
                    molecules["inchi"] == species, ["user_specified_pkas"]
                ] = ",".join(map(str, species_pkas))

    # Find out how each compound can be successfully inserted by sequentially
    # attempting to generate a compound with the following methods
    #   1. Using ChemAxon to generate structure
    #   2. Using user-specified structure
    #   3. Inserting an empty compound
    molecules["compound"] = None
    for method in ["chemaxon", "bypass", "empty"]:
        molecules.loc[molecules["compound"].isnull(), "method"] = method
        molecules.loc[molecules["compound"].isnull(), "compound"] = molecules.loc[
            molecules["compound"].isnull()
        ].apply(_populate_compound_information, axis=1)

    # Rename inchi column, which isn't always inchi, to struct
    molecules = molecules.rename(columns={"inchi": "struct"})
    molecules["status"] = "valid"
    # Remove compounds from chemaxon and empty methods unless requested
    if not bypass_chemaxon:
        molecules.loc[molecules["method"] == "bypass", "compound"] = None
        molecules.loc[molecules["method"] == "bypass", "status"] = "failed"

    if not save_empty_compounds:
        molecules.loc[molecules["method"] == "empty", "compound"] = None
        molecules.loc[molecules["method"] == "empty", "status"] = "failed"

    # Log results
    molecules_string = molecules.to_string(
        columns=["struct", "inchi_key", "method", "status"]
    )
    if any(molecules["compound"].isnull()):
        logger.warning("One or more compounds were unable to be decomposed")
        logger.debug(f"Table of compound creation results\n{molecules_string}")
    else:
        logger.debug(
            "All compounds generated succesfully"
            f"Table of compound creation results\n{molecules_string}"
        )

    cpd_results = [
        GenerateCompoundResult(
            compound=row.compound,
            inchi_key=row.inchi_key,
            method=row.method,
            status=row.status,
            structure=row.struct,
        )
        for row in molecules.itertuples()
    ]

    return cpd_results


def get_or_create_compounds(
    ccache: CompoundCache,
    mol_strings: List[str],
    mol_format: str = "smiles",
    connectivity_only: bool = False,
    bypass_chemaxon: bool = False,
    save_empty_compounds: bool = False,
    specified_pkas: dict = None,
    read_only: bool = False,
) -> List[GenerateCompoundResult]:
    """Get compounds from cache by descriptors, or creates them if missed.

    Parameters
    ----------
    ccache : CompoundCache
        [description]
    mol_strings : List[str]
        A string or list of strings containing text description of the
        molecule(s) (SMILES or InChI)
    mol_format : str, optional
        The format the molecules are given in (smiles, inchi),
        by default "smiles"
    connectivity_only : bool, optional
        Whether to use only connectivity portion of inchi_key when
        searching the ccache for an existing compound, by default False
    bypass_chemaxon : bool, optional
        Allows compounds that fail to be decomposed with chemaxon to be
        created with the user-specified structure instead, by default False
    save_empty_compounds : bool, optional
        Whether to insert compounds into the database that cannot be
        decomposed user-specified structure, by default False
    specified_pkas : dict, optional
            A dictionary of user-specified pkas of form
            {mol_string: [pka1, pka2], ...}
            where mol_string is found in mol_strings, by default dict()
    read_only : bool
        Determines whether to try attempt to create new compounds, or limit
        to existing compounds, by default False

    Returns
    -------
    List[GenerateCompoundResult]
        Compound objects that were obtained from the database or created.
    """
    # InChI key is 3 parts separated by '-', X-Y-Z, where X is connectivity only
    # Y has stereochemical information, and Z describes deprotonation
    if connectivity_only:
        # Only take the connectivity block
        num_splits = 2
    else:
        # Take first two blocks
        num_splits = 1

    cpd_results = []
    missing_compounds_indices = []
    for i, structure in enumerate(mol_strings):
        inchi_key = readstring(mol_format, structure).write("inchikey").strip()
        cc_search = ccache.search_compound_by_inchi_key(
            inchi_key.rsplit("-", num_splits)[0]
        )
        if cc_search:
            # Check if any compounds are in the training data
            training_compound = None
            for result in cc_search:
                if result.id in TRAINING_IDS:
                    training_compound = result
                    break

            if training_compound is None:
                # If no match, use the lowest id number
                training_compound = cc_search[0]

            cpd_results.append(
                GenerateCompoundResult(
                    structure=structure,
                    compound=training_compound,
                    inchi_key=inchi_key,
                    method="database",
                    status="valid",
                )
            )
        elif read_only:
            # this compound was not found in the database
            # and we are in read_only mode so it should not
            # be created
            cpd_results.append(
                GenerateCompoundResult(
                    structure=structure,
                    compound=None,
                    inchi_key=None,
                    method="read-only",
                    status="failed",
                )
            )
        else:
            missing_compounds_indices.append(i)
            # this compound was not found in the database
            # and we are not in read_only more (i.e. it should be
            # created), we add a "Result" for it that will be
            # later filled in with the created Compound data
            cpd_results.append(
                GenerateCompoundResult(
                    structure=structure,
                    compound=None,
                    inchi_key=None,
                    method="",
                    status="",
                )
            )

    if len(missing_compounds_indices) > 0:
        created_cpd_results = create_compounds(
            mol_strings=[mol_strings[j] for j in missing_compounds_indices],
            mol_format=mol_format,
            bypass_chemaxon=bypass_chemaxon,
            save_empty_compounds=save_empty_compounds,
            specified_pkas=specified_pkas,
        )
        for i, j in enumerate(missing_compounds_indices):
            cpd_results[j] = created_cpd_results[i]

    return cpd_results
