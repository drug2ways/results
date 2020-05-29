# Drug2Ways Networks

This folder contains networks used in the Drug2Ways application scenarios. These networks include:

* An In-House network
* OpenBioLink knowledge graph

## In-House Network

The In-House network contains causal interactions (i.e., -1 for decrease and +1 for increase) between the
 following entity types:

* **drug-gene**
* **gene-gene**
* **gene-disease**

Resources used to create this network include the following:
* **drug-gene** interactions were extracted exclusively from [DrugBank](https://www.drugbank.ca/)
* **gene-gene** interactions were extracted from:
    * [BioGRID](https://thebiogrid.org/)
    * [IntAct](https://www.ebi.ac.uk/intact/)
    * [KEGG](https://www.genome.jp/kegg/)
    * [PathwayCommons](https://www.pathwaycommons.org/)
    * [Reactome](https://reactome.org/)
    * [WikiPathways](https://www.wikipathways.org/)
* **gene-disease** interactions were extracted exclusively from [DisGeNET](https://www.disgenet.org/)

## OpenBioLink Knowledge Graph

The [OpenBioLink](https://github.com/OpenBioLink/OpenBioLink) knowledge graph (KG) was used to generate a second network
 used for the Drug2Ways case scenario. The OpenBioLink benchmark dataset is a heterogeneous network incorporating a
 diverse set of biological entities and relations. Causal relationships in the KG have been inferred and simplified to
 -1 for decrease and +1 for increase relationships. 

## Directories

#### Create Networks
In the create_networks directory, you can find notebooks and scripts to generate the In-House pharmacological network or
 the modified OpenBioLink network.

There you can find the following resources:

* The create_custom_network.ipynb generates the In-House pharmacological network, retaining only causal relationships.
* The map_relations.py file contains methods to download the OpenBioLink KG and map interactions between a subset of
 node types to BEL relations.

#### Data 
In the data directory, you can find TSV files containing the interactions found in the In-House and modified OpenBioLink
networks.

There you can find the following resources:

* The custom_network.tsv file contains causal interactions between genes, drugs and diseases derived from the resources
 described above.
* The openbiolink_network.csv file contains causal interactions between genes, drugs, diseases and phenotypes derived
 from the OpenBioLink KG.
