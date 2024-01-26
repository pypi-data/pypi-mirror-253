'''
wrap protein data
'''
import json
import os
from Bio import SeqIO
from .base import Base

class GBK(Base):
    def __init__(self, local_files:str, outdir:str) -> None:
        super().__init__(local_files, outdir)

    def ncbi_rna_gbk(self, molecule_type:str=None):
        '''
        data source: NCBI
        file: *_rna.gbff
        output: json
        '''
        infile = self.get_infile('_rna.gbff')
        if not infile:
            return None
        if molecule_type is None:
            molecule_type = 'RNA'

        n, res = 0, {}
        for rec in SeqIO.parse(infile, 'genbank'):
            if molecule_type in ('RNA', rec.annotations['molecule_type']):
                res[rec.id] = dict([(k, str(v)) for k,v in rec.annotations.items()])
                res[rec.id]['ID'] = rec.id
                n += 1

        outfile = os.path.join(self.outdir, f'{molecule_type}.json')
        with open(outfile, 'w') as f:
            json.dump(res, f, indent=4)
        meta = {
            'infile': infile,
            'outfile': outfile,
            'file_format': 'json',
            'molecule_type': molecule_type,
            'records': n,
        }
        return meta