# -*- coding: utf-8 -*-

"""Methods to prepare OpenBioLink KG for drug2ways analysis."""

import io
import os
import zipfile

import pandas as pd
import requests

"""OpenBioLink Edge types"""

# Causal OpenBioLink edges
OPENBIOLINK_CAUSAL_EDGES = [
    'GENE_ACTIVATION_GENE',
    'DRUG_ACTIVATION_GENE',
    'GENE_PHENOTYPE',
    'DRUG_BINDACT_GENE',
    'DRUG_BINDINH_GENE',
    'GENE_INHIBITION_GENE',
    'GENE_DIS',
    'DRUG_INHIBITION_GENE',
]

# Discarded OpenBioLink edges
OPENBIOLINK_BLACKLIST_EDGES = [
    'DRUG_REACTION_GENE',
    'GENE_CATALYSIS_GENE',
    'GENE_PTMOD_GENE',
    'GENE_DRUG',
    'GENE_EXPRESSION_GENE',
    'GENE_REACTION_GENE',
    'GENE_BINDING_GENE',
    'DRUG_BINDING_GENE',
    'DRUG_CATALYSIS_GENE',
    'GENE_GENE',
    'PART_OF',
    'IS_A',
    'DIS_PHENOTYPE'
]

# OpenBioLink edge type mappings to increases (+1) and decreases (-1) relationships
OPENBIOLINK_EDGE_TYPE_MAPPINGS = {
    'GENE_PHENOTYPE': 1,
    'GENE_ACTIVATION_GENE': 1,
    'DRUG_INHIBITION_GENE': -1,
    'DRUG_ACTIVATION_GENE': 1,
    'GENE_INHIBITION_GENE': -1,
    'GENE_DIS': 1,
    'DRUG_BINDINH_GENE': -1,
    'DRUG_BINDACT_GENE': 1
}

# OpenBioLink graph URL
OPENBIOLINK_DIR_GRAPH_URL = "https://samwald.info/res/OpenBioLink_2020_final/HQ_DIR.zip"

# All true positive edges in default, directed, high-quality OpenBioLink graph
EDGE_FILE = os.path.join('HQ_DIR', 'graph_files', 'edges.csv')


def handle_zipfile_download(path: str) -> None:
    """Download and extract zip file content."""
    r = requests.get(path)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()


def filter_edge_types(path: str, outfile: str):
    """Read and filter edge types file."""
    column_names = ['NODE_1_ID', 'EDGE_TYPE', 'NODE_2_ID', 'QUALITY_SCORE', 'SOURCE']

    df = pd.read_csv(path, sep='\t', names=column_names)

    # Get filtered dataFrame with directed and association type edges
    df = df[df['EDGE_TYPE'].isin(OPENBIOLINK_CAUSAL_EDGES)]

    return _map_edges_to_bel(df, outfile)


def _map_edges_to_bel(df, outfile: str) -> None:
    """Map OpenBioLink edge types to BEL relations."""
    # Create mapping dataFrame from edge type mappings dictionary
    mapping_df = pd.DataFrame(OPENBIOLINK_EDGE_TYPE_MAPPINGS.items(), columns=['EDGE_TYPE', 'RELATION'])

    # Merge original OpenBioLink edge type and mapping dataFrames to get dataFrame of BEL relations
    df_merged = pd.merge(df, mapping_df, on="EDGE_TYPE", how="left")

    openbiolink_df = df_merged[['NODE_1_ID', 'NODE_2_ID', 'RELATION']]

    columns = {'NODE_1_ID': 'source', 'NODE_2_ID': 'target', 'RELATION': 'relation'}

    openbiolink_df = openbiolink_df.rename(columns=columns)

    openbiolink_df.to_csv(outfile, sep='\t', index=False)
