"""
processs FASTQ 
"""
from Bio import SeqIO
from biosequtils import Iterator
import os
import numpy as np
from typing import Iterable
import gzip



class FASTQ:
    def __init__(self):
        self.dir_cache = os.environ.get('DIR_CACHE')

    def parse_records(self, fq_file) -> Iterable:
        if fq_file.endswith('.gz'):
            with gzip.open(fq_file, 'rt') as f:
                for rec in SeqIO.parse(f, 'fastq'):
                    yield rec
        else:
            with open(fq_file, 'r') as f:
                for rec in SeqIO.parse(f, 'fastq'):
                    yield rec

    def parse_pair_records(self, fq1_file:str, fq2_file:str)->Iterable:
        fq1 = self.parse_records(fq1_file)
        fq2 = self.parse_records(fq2_file)
        for rec1, rec2 in zip(fq1, fq2):
            yield (rec1, rec2)

    def quality_scores(self,
            rec_iter:Iterable,
            scores_file:str=None,
            compress:int=None
        ):
        '''
        phred-quality score: 0-60
        export scores matrix
        '''
        if scores_file is None:
            scores_file = os.path.join(self.dir_cache, "quality_scores.txt")
        if compress is None:
            compress = 10
        # retrieve phred scores
        with open(scores_file, 'wt') as f:
            pool = []
            for rec in rec_iter:
                phred_scores = rec.letter_annotations["phred_quality"]
                if len(pool) < compress:
                    pool.append(phred_scores)
                elif len(pool) == compress:
                    Iterator.shape_length(pool, 0)
                    pool = np.array(pool).mean(axis=0)
                    pool = [ "{:.2f}".format(i) for i in pool]
                    scores = '\t'.join([str(i) for i in pool])
                    f.write(f"{scores}\n")
                    pool = []
            else:
                if len(pool) > 0:
                    Iterator.shape_length(pool, 0)
                    pool = np.array(pool).mean(axis=0)
                    pool = [ "{:.2f}".format(i) for i in pool]
                    scores = '\t'.join([str(i) for i in pool])
                    f.write(f"{scores}\n")
        return scores_file

    def trim_polyx(self, tails:list, min_len:int=None):
        '''
        polyX could be polyA or polyG at 3-end
        args: tails could be ['A', 'G']
        '''
        # polyA most 20~250 nt
        if min_len is None:
            min_len = 15

    def is_fastq(self, fq_file:str)->bool:
        '''
        1. file extension is .fastq, or .fq
        2. file exists
        '''
        extension = os.path.basename(fq_file).split('.')[-1]
        if not extension in ('fastq', 'fq'):
            return False
        if not os.path.isfile(fq_file):
            return False
        return True
