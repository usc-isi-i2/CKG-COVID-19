## Entities not in Wikidata

The file is `entities_not_in_wikidata.tsv.gz`, contains information about the entities
mentioned in the CORD-19 corpus, which are not present in Wikidata as of March 30, 2020.

We created custom Qnodes for these entities using the formula,

```
Qnode(entity) = Q00005550- + <entity_type> + -<entity id>
```

We augmented these qnodes with information from the [CTD datasets](http://ctdbase.org/downloads).

Sample,

| id                                       | node1                          | property | node2                                                                                                       |
|------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| Q00005550-disease-MESHC537014-P31-0      | Q00005550-disease-MESHC537014  | P31      | Q12136                                                                                                      |
| Q00005550-disease-MESHC537014-P486-1     | Q00005550-disease-MESHC537014  | P486     | MESH:C537014                                                                                                |
| Q00005550-disease-MESHC537014-label-2    | Q00005550-disease-MESHC537014  | label    | Infantile polyarteritis                                                                                     |
| Q00005550-chemical-MESHC086979-P31-0     | Q00005550-chemical-MESHC086979 | P31      | Q11344                                                                                                      |
| Q00005550-chemical-MESHC086979-P486-1    | Q00005550-chemical-MESHC086979 | P486     | MESH:C086979                                                                                                |
| Q00005550-chemical-MESHC086979-label-2   | Q00005550-chemical-MESHC086979 | label    | arbidol                                                                                                     |
| Q00005550-chemical-MESHC086979-P231-3    | Q00005550-chemical-MESHC086979 | P231     | 131707-23-8                                                                                                 |
| Q00005550-chemical-MESHC086979-aliases-4 | Q00005550-chemical-MESHC086979 | aliases  | 1-methyl-2-((phenylthio)methyl)-3-carbethoxy-4-((dimethylamino)methyl)-5-hydroxy-6-bromindole hydrochloride |
| Q00005550-chemical-MESHC086979-aliases-5 | Q00005550-chemical-MESHC086979 | aliases  | arbidole                                                                                                    |
| Q00005550-chemical-MESHC086979-aliases-6 | Q00005550-chemical-MESHC086979 | aliases  | umifenovir                                                                                                  |
| Q00005550-chemical-MESHC086979-P31-0     | Q00005550-chemical-MESHC086979 | P31      | Q11344                                                                                                      |
| Q00005550-chemical-MESHC086979-P486-1    | Q00005550-chemical-MESHC086979 | P486     | MESH:C086979                                                                                                |
| Q00005550-chemical-MESHC086979-label-2   | Q00005550-chemical-MESHC086979 | label    | arbidol                                                                                                     |
| Q00005550-chemical-MESHC086979-P231-3    | Q00005550-chemical-MESHC086979 | P231     | 131707-23-8                                                                                                 |
| Q00005550-chemical-MESHC086979-aliases-4 | Q00005550-chemical-MESHC086979 | aliases  | 1-methyl-2-((phenylthio)methyl)-3-carbethoxy-4-((dimethylamino)methyl)-5-hydroxy-6-bromindole hydrochloride |
| Q00005550-chemical-MESHC086979-aliases-5 | Q00005550-chemical-MESHC086979 | aliases  | arbidole                                                                                                    |
| Q00005550-chemical-MESHC086979-aliases-6 | Q00005550-chemical-MESHC086979 | aliases  | umifenovir                                                                                                  |
| Q00005550-chemical-MESHC449399-P31-0     | Q00005550-chemical-MESHC449399 | P31      | Q11344                                                                                                      |
| Q00005550-chemical-MESHC449399-P486-1    | Q00005550-chemical-MESHC449399 | P486     | MESH:C449399                                                                                                |