# Scientific Articles not in Wikidata

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
