# CKG Covid-19 

We are building easy to use knowledge graphs (KG) about the scientific articles in the CORD-19 corpus published by the Allen Institute for AI. We integrate the outputs of several state of the art machine reading systems and several bio-informatics databases with Wikidata. To make the KG easy to use, we extracted from Wikidata the subset of items related to the scientifc articles in the CORD-19 corpus. The subset includes the scientific articles in the CORD-19 corpus, plus their citations and the genes, proteins, drugs, diseases, etc. related to them. We map the outputs of the machine reading systems to the Wikidata identifiers, and build an integrated dataset. Our goal is to build the smallest KG that contains useful information in a way that is easy for application developers to consume.

To make the KG easy to use, our primary dataset is published as an edge-list in TSV format. This dataset can be directly imported into Pandas, relational databases, graph software, etc. In addition, we offer the dataset in a public SPARQL endpoint using the Wikidata SPARQL platform, as an RDF dump and as a file that directly imports into Neo4J.


## Covid-19 Dataset

The data files are available to download from the folder `datasets/version_**`, current version is `01`.

All the files in this dataset have the following columns in common:

* `id` - a unique identifier for the rows in the file
* `node1` - subject of the item in a row
* `property` - the property describing the subject
* `node2` - the value or object of the property

We describe the contents and format of the files in the dataset in the following sections.


### Scientific Articles in Wikidata

The file is named `scholarly_articles_in_wikidata.tsv.gz` in the dataset and contains
the information about scientific articles in CORD-19 corpus which are present in Wikidata.

Sample from the file,

| id                | node1     | property | node2                                                                                                                      |
|-------------------|-----------|----------|----------------------------------------------------------------------------------------------------------------------------|
| Q21093209-P698-1  | Q21093209 | P698     | 20663162                                                                                                                   |
| Q21093209-P932-1  | Q21093209 | P932     | 2918564                                                                                                                    |
| Q21093209-P356-1  | Q21093209 | P356     | 10.1186/1743-422X-7-169                                                                                                    |
| Q21093209-P31-1   | Q21093209 | P31      | Q13442814                                                                                                                  |
| Q21093209-P31-2   | Q21093209 | P31      | Q45182324                                                                                                                  |
| Q21093209-P1476-1 | Q21093209 | P1476    | 'RETRACTED: Influenza or not influenza: analysis of a case of high fever that happened 2000 years ago in Biblical time'@en |
| Q21093209-P1433-1 | Q21093209 | P1433    | Q7934868                                                                                                                   |
| Q21093209-P478-1  | Q21093209 | P478     | 7                                                                                                                          |
| Q21093209-P577-1  | Q21093209 | P577     | ^2010-00-00T00:00:00Z/9                                                                                                    |
| Q21093209-P304-1  | Q21093209 | P304     | 169                                                                                                                        |
| Q21093209-P433-1  | Q21093209 | P433     | 1                                                                                                                          |
| Q21093209-P921-1  | Q21093209 | P921     | Q18123741                                                                                                                  |
| Q21093209-P2093-1 | Q21093209 | P2093    | Kam L E Hon                                                                                                                |
| Q21093209-P2093-2 | Q21093209 | P2093    | Pak C Ng                                                                                                                   |
| Q21093209-P2093-3 | Q21093209 | P2093    | Ting F Leung                                                                                                               |
| Q21093209-P2860-1 | Q21093209 | P2860    | Q37646978                                                                                                                  |
| Q21093209-P2860-2 | Q21093209 | P2860    | Q40558423                                                                                                                  |
| Q21093209-P2860-3 | Q21093209 | P2860    | Q53807186                                                                                                                  |
| Q21093209-P2860-4 | Q21093209 | P2860    | Q43175873                                                                                                                  |
 
 
 ### Scientific Articles not in Wikidata
 
 This file, `scholarly_articles_not_in_wikidata.tsv.gz`, contains the information about the scientific
 articles in the CORD-19 corpus which are not present in Wikidata as of March 30, 2020.
 We created customised Qnodes for these articles using the formula,
 
 ```
Qnode(article) = Q00007770 + (Pubmed central or Pubmed Id)
```
We added the information about the articles, for eg: authors, DOI, published year etc.
as found in the CORD-19 dataset using the properties in Wikidata.

Sample from the file,

| id                                           | node1             | property | node2                                                                                                                         |
|----------------------------------------------|-------------------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| Q0000777030612085-P31-30612085&#124;None.json-0   | Q0000777030612085 | P31      | Q13442814                                                                                                                     |
| Q0000777030612085-label-30612085&#124;None.json-1 | Q0000777030612085 | label    | The antiviral activity of arbidol hydrochloride against herpes simplex virus type II (HSV-2) in a mouse model of vaginitis.   |
| Q0000777030612085-P577-30612085&#124;None.json-2  | Q0000777030612085 | P577     | 2019                                                                                                                          |
| Q0000777030612085-P1476-30612085&#124;None.json-3 | Q0000777030612085 | P1476    | The antiviral activity of arbidol hydrochloride against herpes simplex virus type II (HSV-2) in a mouse model of vaginitis.   |
| Q0000777030612085-P698-30612085&#124;None.json-4  | Q0000777030612085 | P698     | 30612085                                                                                                                      |
| Q0000777032111113-P31-32111113&#124;None.json-0   | Q0000777032111113 | P31      | Q13442814                                                                                                                     |
| Q0000777032111113-label-32111113&#124;None.json-1 | Q0000777032111113 | label    | [The keypoints in treatment of the critical coronavirus disease 2019 patient].                                                |
| Q0000777032111113-P577-32111113&#124;None.json-2  | Q0000777032111113 | P577     | 2020                                                                                                                          |
| Q0000777032111113-P1476-32111113&#124;None.json-3 | Q0000777032111113 | P1476    | [The keypoints in treatment of the critical coronavirus disease 2019 patient].                                                |
| Q0000777032111113-P698-32111113&#124;None.json-4  | Q0000777032111113 | P698     | 32111113                                                                                                                      |
| Q0000777031125806-P31-31125806&#124;None.json-0   | Q0000777031125806 | P31      | Q13442814                                                                                                                     |
| Q0000777031125806-label-31125806&#124;None.json-1 | Q0000777031125806 | label    | Nucleoside analogues for the treatment of coronavirus infections.                                                             |
| Q0000777031125806-P577-31125806&#124;None.json-2  | Q0000777031125806 | P577     | 2019                                                                                                                          |
| Q0000777031125806-P1476-31125806&#124;None.json-3 | Q0000777031125806 | P1476    | Nucleoside analogues for the treatment of coronavirus infections.                                                             |
| Q0000777031125806-P698-31125806&#124;None.json-4  | Q0000777031125806 | P698     | 31125806                                                                                                                      |
| Q0000777032096564-P31-32096564&#124;None.json-0   | Q0000777032096564 | P31      | Q13442814                                                                                                                     |
| Q0000777032096564-label-32096564&#124;None.json-1 | Q0000777032096564 | label    | Combination of RT-qPCR Testing and Clinical Features For Diagnosis of COVID-19 facilitates management of SARS-CoV-2 Outbreak. |
| Q0000777032096564-P577-32096564&#124;None.json-2  | Q0000777032096564 | P577     | 2020                                                                                                                          |
| Q0000777032096564-P1476-32096564&#124;None.json-3 | Q0000777032096564 | P1476    | Combination of RT-qPCR Testing and Clinical Features For Diagnosis of COVID-19 facilitates management of SARS-CoV-2 Outbreak. |