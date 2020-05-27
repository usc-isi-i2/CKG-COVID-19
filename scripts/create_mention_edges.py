from glob import glob
import pandas as pd
import json
from scripts.covid_kg_classes import create_scholarly_article
from scripts.covid_kg_classes import TextFragment, Entity, Article, ScholarlyArticle
from typing import List

entity_type_to_wiki_property_map = {
    'species': 'P685',
    'strain': 'P685',
    'chemical': 'P486',
    'disease': 'P486',
    'MESH': 'P486',
    'gene': 'P351',
    'genus': 'P5055'
}

e_type_to_property_map = {
    'gene': 'P2020002',
    'disease': 'P2020003',
    'chemical': 'P2020004',
    'genus': 'P2020005',
    'strain': 'P2020006',
    'species': 'P2020007'
}


class CreateMentionEdges(object):
    def __init__(self, papers_path, identifier_edges_file, ctd_gene_file, ctd_disease_file, ctd_chemical_file):
        self.papers_path = papers_path
        self.identifier_edges_file = identifier_edges_file
        self.ctd_gene_file = ctd_gene_file
        self.ctd_disease_file = ctd_disease_file
        self.ctd_chemical_file = ctd_chemical_file

    def get_papers_list(self):
        return glob('{}/pmid_abs/*json'.format(self.papers_path)) + glob('{}/pmcid/*json'.format(self.papers_path))

    def create_identifier_to_qnode_dict(self):
        id_qnode_dict = {}

        p_df = pd.read_csv(self.identifier_edges_file, sep='\t', dtype=object)
        for i, row in p_df.iterrows():
            id_qnode_dict['{}_{}'.format(row['label'], row['node2'])] = row['node1']

        g_df = pd.read_csv(self.ctd_gene_file, sep='\t', dtype=object)
        for i, row in g_df.iterrows():
            if row['label'] in ('P351', 'P486'):
                id_qnode_dict['{}_{}'.format(row['label'], row['node2'].replace('"', ''))] = row['node1']

        d_df = pd.read_csv(self.ctd_disease_file, sep='\t', dtype=object)
        for i, row in d_df.iterrows():
            if row['label'] in ('P351', 'P486'):
                id_qnode_dict['{}_{}'.format(row['label'], row['node2'].replace('"', ''))] = row['node1']

        c_df = pd.read_csv(self.ctd_chemical_file, sep='\t', dtype=object)
        for i, row in c_df.iterrows():
            if row['label'] in ('P351', 'P486'):
                id_qnode_dict['{}_{}'.format(row['label'], row['node2'].replace('"', ''))] = row['node1']

        return id_qnode_dict

    def build_mention_edges(self):
        papers = self.get_papers_list()
        print('Total number of papers in the corpus: ',len(papers))
        identifier_dict = self.create_identifier_to_qnode_dict()

        articles = []
        scholarly_articles = []
        for paper in papers:
            pj = json.load(open(paper))
            pmcid = None
            full_pmc_id = pj.get('pmcid', None)
            pmc_key = None
            pm_key = None
            if full_pmc_id and 'PMC' in full_pmc_id:
                pmcid = full_pmc_id[3:]
                pmc_key = 'P932_{}'.format(pmcid)

            pmid = pj.get('pmid', None)
            if pmid:
                pmid = str(pmid)
                pm_key = 'P698_{}'.format(pmid)

            qnode = identifier_dict.get(pmc_key, None)
            if not qnode:
                qnode = identifier_dict.get(pm_key, None)
            if not qnode:
                sa = create_scholarly_article(pj, pmid, pmcid)
                qnode = sa.qnode
                scholarly_articles.append(sa)

            if qnode:
                article = Article(qnode)
                passages = pj.get('passages', [])

                for i in range(len(passages)):
                    passage = passages[i]
                    t_qnode = '{}-text-{}'.format(qnode, i)
                    offset = passage.get('offset')
                    label = passage.get('text', '')
                    annotations = passage.get('annotations', [])
                    section = passage['infons']['section']
                    if len(annotations) > 0:
                        text_frag = TextFragment(label, t_qnode, offset, section)
                        article.add_text_frag(text_frag)

                        for annotation in annotations:
                            infons = annotation['infons']
                            e_identifier = infons['identifier']
                            e_type = infons['type'].lower()
                            e_offset = annotation['locations'][0]['offset']
                            e_length = annotation['locations'][0]['length']
                            stated_as = annotation['text']
                            if e_identifier:
                                if 'MESH' in e_identifier or 'OMIM' in e_identifier:
                                    e_identifier = e_identifier.split(':')[1]
                                e_key = '{}_{}'.format(entity_type_to_wiki_property_map.get(e_type, "None"),
                                                       e_identifier)
                                e_qnode = identifier_dict.get(e_key, None)
                                if e_qnode:
                                    entity = Entity(e_offset, e_length, 'http://blender.cs.illinois.edu/', stated_as,
                                                    text_frag,
                                                    e_type, e_qnode)

                                    article.add_entity(entity)

                articles.append(article)

        return articles, scholarly_articles

    def create_kgtk_format(self, articles: List[Article], scholarly_articles: List[ScholarlyArticle]):
        statements = list()
        qualifiers = list()
        paper_wikidata = list()

        for article in articles:
            a_s = article.serialize()
            qnode = a_s['qnode']

            tfs = a_s['text_fragments']
            entities = a_s['entities']

            for i in range(len(entities)):
                entity = entities[i]
                e_node = entity['qnode']
                e_prop = e_type_to_property_map[entity['type']]
                e_edge_id = '{}-{}-{}'.format(qnode, e_prop, i)
                statements.append({'node1': qnode, 'label': e_prop, 'node2': e_node, 'id': e_edge_id})
                c = 0
                for k in entity:
                    if k not in ('qnode', 'type'):
                        qualifiers.append({'node1': e_edge_id, 'label': k, 'node2': entity[k],
                                           'id': '{}-{}'.format(e_edge_id, c)})
                        c += 1

            for i in range(len(tfs)):
                tf = tfs[i]
                t_node = tf['qnode']
                t_edge_id_prop = '{}-{}-{}'.format(qnode, 'P2020001', i)
                t_label_edge_id = '{}-{}-{}'.format(t_node, 'label', i)
                t_p31_edge_id = '{}-{}-{}'.format(t_node, 'P31', i)
                statements.append({'node1': qnode, 'label': 'P2020001', 'node2': t_node, 'id': t_edge_id_prop})
                statements.append(
                    {'node1': t_node, 'label': 'P2020012', 'node2': tf['P2020012'], 'id': t_label_edge_id})
                statements.append({'node1': t_node, 'label': 'P31', 'node2': tf['P31'], 'id': t_p31_edge_id})
                c = 0
                for k in tf:
                    if k not in ('qnode', 'P2020012', 'P31'):
                        qualifiers.append({'node1': t_edge_id_prop, 'label': k, 'node2': tf[k],
                                           'id': '{}-{}'.format(t_edge_id_prop, c)})
                        c += 1

        for scholarly_article in scholarly_articles:
            sa = scholarly_article.serialize()
            qnode = sa['qnode']
            i = 0
            for k in sa:
                if k not in ('qnode'):

                    if k == 'P2093':
                        authors = sa[k]
                        for author in authors:
                            edge_id = '{}-{}-{}'.format(qnode, k, i)
                            paper_wikidata.append({'node1': qnode, 'label': k, 'node2': author['name'], 'id': edge_id})
                            # series ordinal for authors
                            paper_wikidata.append({'node1': edge_id, 'label': 'P1545', 'node2': author['ordinal'],
                                                   'id': '{}-1'.format(edge_id)})
                            i += 1
                    else:
                        edge_id = '{}-{}-{}'.format(qnode, k, i)
                        paper_wikidata.append({'node1': qnode, 'label': k, 'node2': sa[k], 'id': edge_id})
                        i += 1

        return pd.DataFrame(statements), pd.DataFrame(qualifiers), pd.DataFrame(paper_wikidata)

    def create_mention_edges(self, output_path):
        articles, scholarly_articles = self.build_mention_edges()
        statements, qualifiers, papers_w = self.create_kgtk_format(articles, scholarly_articles)
        statements.to_csv('{}/covid_kgtk_blender_mentions.tsv'.format(output_path), sep='\t', index=False)
        qualifiers.to_csv('{}/covid_kgtk_blender_mentions_qualifiers.tsv'.format(output_path), sep='\t', index=False)
        papers_w.to_csv('{}/scholarly_articles_not_in_wikidata.tsv'.format(output_path), sep='\t', index=False,
                        header=True,
                        columns=['id', 'node1', 'label', 'node2'])
        print('Done!')
