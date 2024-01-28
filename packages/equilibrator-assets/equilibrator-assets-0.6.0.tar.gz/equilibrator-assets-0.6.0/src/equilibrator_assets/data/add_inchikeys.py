# The MIT License (MIT)
#
# Copyright (c) 2018 Institute for Molecular Systems Biology, ETH Zurich.
# Copyright (c) 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark
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


"""A script for filling in missing data in the magnesium_pkds table."""

import argparse
import os
import sys

import pandas as pd
from equilibrator_cache import create_compound_cache_from_sqlite_file


parser = argparse.ArgumentParser(description="add missing n_h values.")
parser.add_argument("cache_path", type=str, help="path to the custom compound cache")
args = parser.parse_args()

cc = create_compound_cache_from_sqlite_file(args.cache_path)

if not os.path.exists("magnesium_pkds.csv"):
    raise FileNotFoundError("Cannot find magnesium_pkds.csv")

mg_df = pd.read_csv("magnesium_pkds.csv")

# fill in the missing values in the n_h column
for idx, row in mg_df.iterrows():
    inchi1, inchi2, inchi3 = row.inchi_key.split("-")

    cpds = cc.search_compound_by_inchi_key(f"{inchi1}-{inchi2}")
    assert (
        len(cpds) > 0
    ), f"Cannot find InChIKey for {row.compound_id}: {inchi1}-{inchi2}"
    if len(cpds) > 1:
        cpds = cc.search_compound_by_inchi_key(f"{inchi1}-{inchi2}-{inchi3}")
        assert (
            len(cpds) > 0
        ), f"Cannot find InChIKey for {row.compound_id}: {inchi1}-{inchi2}-{inchi3}"
        assert (
            len(cpds) <= 1
        ), f"Ambiguous InChIKey for {row.compound_id}: {inchi1}-{inchi2}-{inchi3}"
    cpd = cpds[0]
    if cpd.inchi_key != row.inchi_key:
        sys.stderr.write(
            f"updating InChIKey in the mg table {row.inchi_key} -> {cpd.inchi_key}\n"
        )
        mg_df.at[idx, "inchi_key"] = cpd.inchi_key

    # net_charge = n_h + 2*n_mg - n_e
    expected_n_h = (
        row.charge
        - cpds[0].net_charge
        - 2 * (row.n_mg - 1)
        + cpds[0].atom_bag.get("H", 0)
    )
    if pd.isnull(row.n_h):
        mg_df.at[idx, "n_h"] = expected_n_h
    elif row.n_h != expected_n_h:
        sys.stderr.write(
            f"inconsistent pseudoisomer values in "
            f"row #{idx}: compound = {row.compound_id}"
        )

mg_df.to_csv("magnesium_pkds_final.csv")
