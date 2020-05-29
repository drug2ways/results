# Validation with ClinicalTrials.org
This directory contains the mappings of clinical trials from ClinicalTrials.org.

1. We reproduced the following [notebook](https://github.com/dhimmel/clintrials/blob/master/1.clinical-trials.ipynb) to
   retrieve all MeSH intervention (drugs) and MeSH condition (disease) from all clinical trials downloaded on 16-04-2020

2. The second step was to map MeSH interventions to DrugBank/PubChem identifiers using information from DrugCentral
   (data/identifiers.tsv) depending on the network (see both files in the data directory). This mapping determins which
   drugs will be used as source nodes for validation.

3. Mapping MeSH terms for each network (conditions)
- To map the indications in MeSH from the clinicaltrials.gov file to the custom network which contains UMLS CUIs, we
  used the mappings from DisGeNet and convert from MeSH to UMLS. See notebooks/custom_network_validation.ipynb
- To map the indications in MeSH from the clinicaltrials.gov file to the OpenBioLink which contains DO ids for diseases,
  we used the cross-references from Disease Ontology (DO). See notebooks/openbiolink_network_validation.ipynb
   