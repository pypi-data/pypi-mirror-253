"""
ASCT+B parser script
"""

from re import match

import pandas as pd


def parse_asctb(asctb_json: dict) -> pd.DataFrame:
    """
    Takes ASCT-b JSON as input;
    Processes only AS (anatomy) and CT (cell type) columns.
    RETURN
    Pandas DataFrame with columns ['o', 's', 'olabel', 'slabel', user_olabel, user_slabel]
    where each pair of adjacent columns => a subject-object pair for testing
    """

    def check_id(term_id):
        return match(r"(CL|UBERON|PCL)\:[0-9]+", term_id)

    dataframe = []

    for row in asctb_json:
        # AS-AS RELATIONSHIP
        anatomical_structures = row['anatomical_structures']
        for current, nex in zip(anatomical_structures, anatomical_structures[1:]):
            if check_id(current['id']) and check_id(nex['id']):
                d = {}
                d['s'] = nex['id']
                d['slabel'] = nex['rdfs_label']
                d['user_slabel'] = nex['name']
                d['o'] = current['id']
                d['olabel'] = current['rdfs_label']
                d['user_olabel'] = current['name']
                dataframe.append(d)

        # CT-CT RELATIONSHIP
        cell_types = row['cell_types']
        for current, nex in zip(cell_types, cell_types[1:]):
            if check_id(current['id']) and check_id(nex['id']):
                d = {}
                d['s'] = nex['id']
                d['slabel'] = nex['rdfs_label']
                d['user_slabel'] = nex['name']
                d['o'] = current['id']
                d['olabel'] = current['rdfs_label']
                d['user_olabel'] = current['name']
                dataframe.append(d)

        # CT-AS RELATIONSHIP
        if len(anatomical_structures) > 0 and len(cell_types) > 0:
            last_as = anatomical_structures[-1]
            if not check_id(last_as['id']) and len(anatomical_structures) > 1:
                last_as = anatomical_structures[-2]
            last_ct = cell_types[-1]
            if not check_id(last_ct['id']) and len(cell_types) > 1:
                last_ct = cell_types[-2]
            if check_id(last_as['id']) and check_id(last_ct['id']):
                d = {}
                d['s'] = last_ct['id']
                d['slabel'] = last_ct['rdfs_label']
                d['user_slabel'] = last_ct['name']
                d['o'] = last_as['id']
                d['olabel'] = last_as['rdfs_label']
                d['user_olabel'] = last_as['name']
                dataframe.append(d)

    return pd.DataFrame.from_records(dataframe).drop_duplicates()
