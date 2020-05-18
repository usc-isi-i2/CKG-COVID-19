from tqdm import tqdm
import json
from glob import glob

pmcid_path = "/Users/amandeep/Documents/pmcid"
pubmed_path = "/Users/amandeep/Documents/pmid_abs"

seen = {}


def pubmed_analysis():
    """
    find out which papers in the corpus are not in Wikidata
    :return:
    """

    corpus_identifiers_f = open('corpus-identifiers.tsv', 'w')
    corpus_identifiers_f.write('node2\tlabel\n')

    ids_dict = {
        'species': 'P685',
        'strain': 'P685',
        'chemical': 'P486',
        'disease': 'P486',
        'MESH': 'P486',
        'gene': 'P351',
        'genus': 'P5055'
    }

    for f in tqdm(glob('{}/*json'.format(pmcid_path)) + glob('{}/*json'.format(pubmed_path))):

        x = json.load(open(f))

        pmcid = x.get('pmcid', None)  # P932
        if pmcid:
            if pmcid not in seen:
                seen[pmcid] = 1

                if 'PMC' in pmcid:
                    corpus_identifiers_f.write('{}\t{}\n'.format(json.dumps(pmcid[3:]), 'P932'))
                else:
                    corpus_identifiers_f.write('{}\t{}\n'.format(json.dumps(pmcid), 'P932'))

        pmid = x.get('pmid', None)  # P698
        if pmid:
            pmid = str(pmid)
            if pmid not in seen:
                seen[pmid] = 1
                corpus_identifiers_f.write('{}\t{}\n'.format(json.dumps(pmid), 'P698'))

        passages = x.get('passages', [])

        for i in range(len(passages)):
            passage = passages[i]
            annotations = passage.get('annotations', [])
            if len(annotations) > 0:
                for annotation in annotations:

                    infons = annotation['infons']
                    identifiers = infons['identifier']
                    type = infons['type'].lower()
                    if identifiers:
                        if ';' in identifiers:
                            identifiers = identifiers.split(';')
                        if not isinstance(identifiers, list):
                            identifiers = [identifiers]

                        for identifier in identifiers:
                            if type in ids_dict:
                                if identifier:
                                    if '{}@{}'.format(type, identifier) not in seen:
                                        seen['{}@{}'.format(type, identifier)] = 1

                                        if 'MESH' in identifier:
                                            corpus_identifiers_f.write(
                                                '{}\t{}\n'.format(json.dumps(identifier[5:]), ids_dict[type]))
                                        else:
                                            corpus_identifiers_f.write(
                                                '{}\t{}\n'.format(json.dumps(identifier), ids_dict[type]))


pubmed_analysis()
