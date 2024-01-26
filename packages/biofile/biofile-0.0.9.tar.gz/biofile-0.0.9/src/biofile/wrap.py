
import json
import os

from .genome.fasta_dna import FastaDNA
from .genome.gff import GFF


class Wrap:

    def __init__(self, local_files:list, outdir:str=None):
        self.local_files = local_files
        self.outdir = outdir
        self.output_json = os.path.join(self.outdir, 'output.json') \
            if self.outdir and os.path.isdir(self.outdir) else ''

    def load_output(self) -> list:
        if os.path.isfile(self.output_json):
            with open(self.output_json, 'r') as f:
                return json.load(f)
        return []

    def save_output(self, meta:list, overwrite:bool=None) -> list:
        output = [] if overwrite else self.load_output()
        output += meta
        # save
        with open(self.output_json, 'w') as f:
            json.dump(output, f, indent=4)
        return output

    def ncbi_fa_gff(self) -> list:
        '''
        parse sequence and annotations
        retreive NCBI molecular annotations
        '''
        meta = []
        fd = FastaDNA(self.local_files, self.outdir)
        # RNA.fna
        meta_fa_rna = fd.ncbi_rna_dna()
        meta.append(meta_fa_rna)
        # mRNA.fna
        meta_fa_mrna = fd.ncbi_rna_dna('mRNA')
        meta.append(meta_fa_mrna)
        # CDS.fna
        meta_fa_cds = fd.ncbi_cds()
        meta.append(meta_fa_cds)
        # pseudogene.fna
        meta_fa_pseudo = fd.ncbi_pseudo()
        meta.append(meta_fa_pseudo)

        gff_file = fd.get_infile('_genomic.gff')
        if gff_file:
            gff = GFF(gff_file, self.outdir)
            meta_gff_rna = gff.retrieve_RNA()
            if meta_gff_rna:
                meta.append(meta_gff_rna)
            meta_gff_mrna = gff.retrieve_mRNA()
            if meta_gff_mrna:
                meta.append(meta_gff_mrna)
            meta_gff_cds = gff.retrieve_CDS()
            if meta_gff_cds:
                meta.append(meta_gff_cds)
            meta_gff_pseudo = gff.retrieve_pseudo()
            if meta_gff_pseudo:
                meta.append(meta_gff_pseudo)
        return meta
