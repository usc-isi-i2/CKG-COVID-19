# CKG Covid-19 

We are building easy to use knowledge graphs (KG) about the scientific articles in the CORD-19 corpus published by the Allen Institute for AI. We integrate the outputs of several state of the art machine reading systems and several bio-informatics databases with Wikidata. To make the KG easy to use, we extracted from Wikidata the subset of items related to the scientifc articles in the CORD-19 corpus. The subset includes the scientific articles in the CORD-19 corpus, plus their citations and the genes, proteins, drugs, diseases, etc. related to them. We map the outputs of the machine reading systems to the Wikidata identifiers, and build an integrated dataset. Our goal is to build the smallest KG that contains useful information in a way that is easy for application developers to consume.

To make the KG easy to use, our primary dataset is published as an edge-list in TSV format. This dataset can be directly imported into Pandas, relational databases, graph software, etc. In addition, we offer the dataset in a public SPARQL endpoint using the Wikidata SPARQL platform, as an RDF dump and as a file that directly imports into Neo4J.


## Covid-19 KG

![Covid-19 Knowledge Graph](covid_kg_diagram.png "Covid-19 Knowledge Graph")

## Covid-19 Dataset

The data files are available to download from the folder `datasets/version_**`, current version is `01`.

All the files in this dataset have the following columns in common:

* `id` - a unique identifier for the rows in the file
* `node1` - subject of the item in a row
* `property` - the property describing the subject
* `node2` - the value or object of the property

We describe the contents and format of the files in the dataset in the following sections.


- [Scientific Articles in Wikidata](scientific_articles_in_wikidata.md)
- [Scientific Articles not in Wikidata](scientific_articles_not_in_wikidata.md)
- [Entities in Wikidata](entities_in_wikidata.md)
- [Entities not in Wikidata](entities_not_in_wikidata.md)
- [Qualifiers for Scientific Articles and Entities in wikidata](qualifiers_wikidata_kgtk.md)
- [Blender Mentions](covid_kgtk_blender_mentions_with_labels.md)
- [Blender Mentions Qualifiers](entities_not_in_wikidata.md)





