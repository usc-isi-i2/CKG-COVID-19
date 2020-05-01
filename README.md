# CKG-COVID-19

We are building easy to use knowledge graphs (KG) about the scientific articles in the CORD-19 corpus published by the Allen Institute for AI. We integrate the outputs of several state of the art machine reading systems and several bio-informatics databases with Wikidata. To make the KG easy to use, we extracted from Wikidata the subset of items related to the scientifc articles in the CORD-19 corpus. The subset includes the scientific articles in the CORD-19 corpus, plus their citations and the genes, proteins, drugs, diseases, etc. related to them. We map the outputs of the machine reading systems to the Wikidata identifiers, and build an integrated dataset. Our goal is to build the smallest KG that contains useful information in a way that is easy for application developers to consume.

To make the KG easy to use, our primary dataset is published as an edge-list in TSV format. This dataset can be directly imported into Pandas, relational databases, graph software, etc. In addition, we offer the dataset in a public SPARQL endpoint using the Wikidata SPARQL platform, as an RDF dump and as a file that directly imports into Neo4J.

Links to the downloads will be published in the first week of May, 2020.
