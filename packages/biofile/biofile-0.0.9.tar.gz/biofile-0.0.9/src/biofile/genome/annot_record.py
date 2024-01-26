"""
define annotation record: one recored, and one line in GTF/GFF
"""
import re

class AnnotRecord:
    # column 1-9 in GTF/GFF
    names = ['seqid', 'source', 'feature', 'start', 'end', \
        'score', 'strand', 'phase', 'attributes',]

    def __init__(self):
        self.seqid = None
        self.source = None
        self.feature = None
        self.start = None
        self.end = None
        self.score = None
        self.strand = None
        self.phase = None
        self.attributes = None

    def parse(self, record_line:str):
        items = record_line.split('\t')
        for k,v in zip(self.names, items):
            setattr(self, k, v)
        if self.start:
            self.start = int(self.start)
        if self.end:
            self.end = int(self.end)
        return self

    def to_dict(self) -> dict:
        return dict([(k, getattr(self, k)) for k in self.names])

    def to_dict_simple(self) -> dict:
        names = ['seqid', 'start', 'end', 'strand',]
        return dict([(k, getattr(self, k)) for k in names])

    @staticmethod
    def parse_gtf_attributes(attributes:str):
        '''
        GTF attributes
        '''
        names = re.findall('([a-zA-Z0-9_]+)\\s\"', attributes)
        values = re.findall('\"([a-zA-Z0-9_\\.\\%\\:\\(\\)\\-\\,\\/\\s]*?)\"', attributes)
        attr_list = [{'name': k, 'value': v} for k, v in zip(names, values)]
        return attr_list
    
    @staticmethod
    def parse_gff_attributes(attributes):
        '''
        GFF attributes
        '''
        names = re.findall('([a-zA-Z0-9_]+)=', attributes)
        values = re.findall('=([a-zA-Z0-9_\\.\\s\\:\\/\\-\\%\\(\\)\\,\'\\[\\]\\{\\}]+)', attributes)
        attr_list = []
        for k, v in zip(names, values):
            if k == 'Dbxref' and ',' in v:
                for v2 in v.split(','):
                    attr_list.append({'name': k, 'value': v2})
            else:
                attr_list.append({'name': k, 'value': v})
        return attr_list

    @staticmethod
    def map_gff_attributes(attributes):
        '''
        GFF attributes
        '''
        names = re.findall('([a-zA-Z0-9_]+)=', attributes)
        values = re.findall('=([a-zA-Z0-9_\\.\\s\\:\\/\\-\\%\\(\\)\\,\'\\[\\]\\{\\}]+)', attributes)
        attr = {}
        for k, v in zip(names, values):
            if k == 'Dbxref' and ',' in v:
                for sub_feature in v.split(','):
                    sub_k, sub_v = sub_feature.split(':', 1)
                    attr[sub_k] = sub_v
            else:
                attr[k] = v
        return attr
