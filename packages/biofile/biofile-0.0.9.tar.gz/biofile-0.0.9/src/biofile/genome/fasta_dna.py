'''
1. format *.fna to *.fa:
example: >id
        ....
'''
from Bio import SeqIO
import os
import re
from .base import Base

class FastaDNA(Base):
    def __init__(self, local_files:str, outdir:str) -> None:
        super().__init__(local_files, outdir)

    def ncbi_rna_dna(self, molecular_type:str=None):
        '''
        args: molecular_type: RNA, mRNA
        data source: NCBI
        file: *_rna.fna
        output: RNA.fna or mRNA.fna
        '''
        infile = self.get_infile('_rna.fna')
        if not infile:
            return None
        if molecular_type is None:
            molecular_type = 'RNA'

        n = 0
        outfile = os.path.join(self.outdir, f'{molecular_type}.fna')
        with open(outfile, 'w') as f:
            for rec in SeqIO.parse(infile, 'fasta'):
                if molecular_type == 'RNA' or molecular_type in rec.description:
                    rec.description = ''
                    SeqIO.write(rec, f, 'fasta-2line')
                    n += 1
        meta = {
            'infile': infile,
            'outfile': outfile,
            'file_format': 'fna',
            'molecular_type': molecular_type,
            'records': n,
        }
        return meta

    def ncbi_cds(self):
        '''
        data source: NCBI
        file: *_cds_from_genomic.fna
        output: CDS.fna
        '''
        molecular_type = 'CDS'
        infile = self.get_infile('_cds_from_genomic.fna')
        if not infile:
            return None

        n,m = 0, 0
        outfile = os.path.join(self.outdir, f'{molecular_type}.fna')
        with open(outfile, 'w') as f:
            for rec in SeqIO.parse(infile, 'fasta'):
                protein_id = re.findall('\\[protein_id=([A-Z_0-9\\.]*)\\]', str(rec.description))
                if protein_id:
                    rec.id = protein_id[0] 
                    rec.description = ''
                    SeqIO.write(rec, f, 'fasta-2line')
                    n += 1
                else:
                    m += 1
        meta = {
            'infile': infile,
            'outfile': outfile,
            'file_format': 'fna',
            'molecular_type': molecular_type,
            'records': n,
            # pseudo, curated genomic CDS are excluded
            'records_others': m,
        }
        return meta

    def ncbi_pseudo(self):
        '''
        data source: NCBI
        file: *_pseudo_without_product.fna
        output: pseudo.fna
        '''
        molecular_type = 'pseudogene'
        infile = self.get_infile('_pseudo_without_product.fna')
        if not infile:
            return None

        n = 0
        outfile = os.path.join(self.outdir, f'{molecular_type}.fna')
        with open(outfile, 'w') as f:
            for rec in SeqIO.parse(infile, 'fasta'):
                rec.id = rec.id.split('|')[-1]
                rec.description = ''
                SeqIO.write(rec, f, 'fasta-2line')
                n += 1
        meta = {
            'infile': infile,
            'outfile': outfile,
            'file_format': 'fna',
            'molecular_type': molecular_type,
            'records': n,
        }
        return meta
