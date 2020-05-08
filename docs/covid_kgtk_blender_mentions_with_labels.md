## Blender Mentions

The file, `covid_kgtk_blender_mentions_with_labels.tsv.gz`, contains the new property edges as per the
[Covid-19 KG diagram](index.md#covid_kg_diagram).

In addition to the the columns `id`, `node1`, `property` and `node`, this file contains
3 more columns,

- `node1_label`: `node1` label, where available
- `property_label`: `property` label, where available
- `node2_label`: `node2` label, where available

Sample, 

| node1             | property | node2                    | id                                              | node1_label | node2_label | property_label     |
|-------------------|----------|--------------------------|-------------------------------------------------|-------------|-------------|--------------------|
| Q0000777012788592 | P2020001 | Q0000777012788592-text-0 | Q0000777012788592-P2020001-12788592&#124;None.json-0 |             |             | 'Text Fragment'@en  |
| Q0000777019837249 | P2020001 | Q0000777019837249-text-0 | Q0000777019837249-P2020001-19837249&#124;None.json-0 |             |             | 'Text Fragment'@en |
| Q0000777019914509 | P2020001 | Q0000777019914509-text-0 | Q0000777019914509-P2020001-19914509&#124;None.json-0 |             |             | 'Text Fragment'@en |
| Q0000777022951009 | P2020001 | Q0000777022951009-text-0 | Q0000777022951009-P2020001-22951009&#124;None.json-0 |             |             | 'Text Fragment'@en |
| Q0000777022951009 | P2020001 | Q0000777022951009-text-1 | Q0000777022951009-P2020001-22951009&#124;None.json-1 |             |             | 'Text Fragment'@en |
| Q0000777027133972 | P2020001 | Q0000777027133972-text-0 | Q0000777027133972-P2020001-27133972&#124;None.json-0 |             |             | 'Text Fragment'@en |
| Q0000777027133972 | P2020001 | Q0000777027133972-text-1 | Q0000777027133972-P2020001-27133972&#124;None.json-1 |             |             | 'Text Fragment'@en |
| Q0000777028236402 | P2020001 | Q0000777028236402-text-0 | Q0000777028236402-P2020001-28236402&#124;None.json-0 |             |             | 'Text Fragment'@en |
| Q0000777028236402 | P2020001 | Q0000777028236402-text-1 | Q0000777028236402-P2020001-28236402&#124;None.json-1 |             |             | 'Text Fragment'@en |