"""
process GFF file
https://www.ncbi.nlm.nih.gov/genbank/genomes_gff/

"""
import json
from .annot_record import AnnotRecord
from .annot_file import AnnotFile

class GTF(AnnotFile):
    def __init__(self, gtf_file:str, outdir:str=None):
        super().__init__(gtf_file, outdir)

    def split_by_feature(self, parse_attributes:bool=None):
        '''
        split annotations by feature (in 3rd column)
        convert annotations to json by feature
        '''
        if not parse_attributes:
            parse_attributes = False
        annot = {}
        for line in self.iterator():
            c = AnnotRecord().parse(line)
            if parse_attributes:
                c.attributes = AnnotRecord.parse_gtf_attributes(c.attributes)
            rec = c.to_dict()
            feature = rec['feature']
            if feature not in annot:
                annot[feature] = []
            annot[feature].append(rec)

        res = self.to_json_files(annot)
        return res

    def parse_attributes(self, attr:str, feature:str=None, file_name:str=None) -> dict:
        feature = '_all_' if feature is None else feature
        file_name = f"{attr}_{feature}" if file_name is None else file_name

        annot = {}
        for line in self.iterator():
            key = None
            c = AnnotRecord().parse(line)
            item = c.to_dict_simple()
            attributes = AnnotRecord.parse_gtf_attributes(c.attributes)
            for i in attributes:
                if i['name'] == 'db_xref' and ':' in i['value']:
                    _items = i['value'].split(':')
                    name2, value2 = _items[0], _items[-1]
                    item[name2] = value2
                    if attr == name2:
                        key = value2
                else:
                    item[i['name']] = i['value']
                    if attr == i['name']:
                        key = i['value']
            if key and feature in ('_all_', c.feature):
                curr = annot.get(key, {})
                for k, v in item.items():
                    v = str(v)
                    if k in curr:
                        if v not in curr[k]:
                            curr[k] += f",{v}"
                    else:
                        curr[k] = v
                annot[key] = curr
        if annot:
            self.to_text(annot, file_name)
        return annot


    def lift_attribute(self, name:str=None):
        '''
        args: infile should be one feature in json format
        args: attr_name should be one of names 
            in the 9th column known as attributes.
        '''
        if name is None:
            name = 'ID'
        res = {}
        with open(self.infile, 'r') as f:
            for record in json.load(f):
                attr = AnnotRecord.parse_gtf_attributes(record['attributes'])
                for item in attr:
                    if (item['name'] == name or name in item['value']) and item['value']:
                        record['ID'] = item['value']
                        res[item['value']] = record
                        break
        return res                          

