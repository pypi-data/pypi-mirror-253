import json
import os
import pandas as pd
from typing import Iterable


class AnnotFile:
    def __init__(self, infile:str, outdir:str=None):
        self.infile = infile
        self.outdir = outdir

    def iterator(self) -> Iterable:
        if not os.path.isfile(self.infile):
            return None
        with open(self.infile, 'r') as f:
            for line in f:
                if not line.startswith('#'):
                    yield line.rstrip()

    def to_json_files(self, annot:dict):
        '''
        annot: key~value: file name ~ records in list
        '''
        res = {}
        for feature, records in annot.items():
            if self.outdir and os.path.isdir(self.outdir):
                outfile = os.path.join(self.outdir, f"{feature}.json")
                with open(outfile, 'w') as f:
                    json.dump(records, f, indent=4)
                res[feature] = outfile
            else:
                res[feature] = len(records)
        return res
    
    def to_text(self, annot:dict, file_name):
        df = pd.DataFrame(annot).sort_index(axis=0).sort_index(axis=1)
        if self.outdir and os.path.isdir(self.outdir):
            outfile = os.path.join(self.outdir, f"{file_name}.txt")
            df.to_csv(outfile, sep='\t', header=True, \
                index=True, index_label='attributes')
    
    def to_json(self, annot:dict, molecular_type:str):
        outfile = os.path.join(self.outdir, f"{molecular_type}.json")
        with open(outfile, 'w') as f:
            json.dump(annot, f, indent=4)
        meta = {
            'infile': self.infile,
            'outfile': outfile,
            'file_format': 'json',
            'molecular_type': molecular_type,
            'records': len(annot),
        }
        return meta
