from typing import List


class TextFragment(object):
    def __init__(self, label, qnode, offset, section):
        self.text = label
        self.qnode = qnode
        self.offset = offset
        self.section = section
        self.P31 = 'Q1385610'

    def serialize(self):
        return {
            'P2020012': self.text,
            'qnode': self.qnode,
            'P4153': self.offset,
            'P958': self.section,
            'P31': self.P31
        }


class Entity(object):
    def __init__(self, offset, length, attributed_to, stated_as, text_fragment: TextFragment, type, qnode):
        self.offset = offset
        self.length = length
        self.attributed_to = attributed_to
        self.stated_as = stated_as
        self.text_fragment = text_fragment
        self.type = type
        self.qnode = qnode

    def serialize(self):
        return {
            'P4153': self.offset,
            'P2043': self.length,
            'P1932': self.stated_as,
            'P2020008': self.attributed_to,
            'P2020001': self.text_fragment.qnode,
            'type': self.type,
            'qnode': self.qnode
        }


class Article(object):
    def __init__(self, qnode):
        self.qnode = qnode
        self.text_frags = []
        self.entities = []

    def add_text_frag(self, text_frag: TextFragment):
        self.text_frags.append(text_frag)

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def serialize(self):
        tfs = []
        ens = []
        s = {}
        for tf in self.text_frags:
            tfs.append(tf.serialize())

        for entity in self.entities:
            ens.append(entity.serialize())

        s['text_fragments'] = tfs
        s['entities'] = ens
        s['qnode'] = self.qnode
        return s


class Author(object):
    def __init__(self, first_name, surname, ordinal):
        self.name = '{}, {}'.format(surname, first_name)
        self.ordinal = ordinal

    def serialize(self):
        return {'name': self.name, 'ordinal': self.ordinal}


class ScholarlyArticle(object):
    def __init__(self, title, authors: List[Author], publication_date, pmc_id, pm_id, doi):
        self.P31 = 'Q13442814'  # instance of
        self.P1476 = title  # title
        self.label = title
        self.P2093 = authors  # author name string
        self.P577 = publication_date  # publication date
        self.P932 = pmc_id
        self.P698 = pm_id
        self.P356 = doi
        self.qnode = self.create_qnode()

    def create_qnode(self):
        qnode = None
        if self.P932:
            qnode = 'Q00007770{}'.format(self.P932)
        elif self.P698:
            qnode = 'Q00007770{}'.format(self.P698)
        return qnode

    def serialize(self):
        _d = {'P31': self.P31, 'label': self.label, 'qnode': self.qnode}
        if self.P577:
            _d['P577'] = self.P577
        if self.P1476:
            _d['P1476'] = self.P1476

        if self.P2093:
            _d['P2093'] = [author.serialize() for author in self.P2093]
        if self.P932:
            _d['P932'] = self.P932
        if self.P698:
            _d['P698'] = self.P698
        if self.P356:
            _d['P356'] = self.P356
        return _d


def create_scholarly_article(paper_json, pmid, pmc_id):
    published_date = paper_json.get('year')
    passages = paper_json.get('passages', [])
    title = ""
    doi = None
    authors = []
    if not isinstance(passages, list):
        passages = [passages]
    for passage in passages:
        infons = passage.get('infons', None)
        if infons:
            if infons['section'].lower() == 'title':
                doi = infons.get('article-id_doi', None)
                title = passage['text']

                for k in infons:
                    if k.startswith('name_'):
                        authors.append(create_author_kg(k, infons[k]))

                break

    return ScholarlyArticle(title, authors, published_date, pmc_id, pmid, doi)


def create_author_kg(field, value):
    ordinal = int(field.split('_')[1])
    first_name = ''
    surname = ''
    names = value.split(';')
    for name in names:
        if name.startswith('given-names:'):
            first_name = name.split(':')[1]
        if name.startswith('surname:'):
            surname = name.split(':')[1]
    return Author(first_name, surname, ordinal)
