'''
'''
import json
import os
from Bio import SeqIO

class AnnotValidate:

    @staticmethod
    def ID_fasta_vs_json(fa_file:str, json_file:str):
        '''
        record.id in fasta should match key in json.
        records of json could be more then fasta records
        '''
        fa_ids, shared = [], []
        with open(json_file, 'r') as f1, open(fa_file, 'r') as f2:
            json_data = json.load(f1)
            for rec in SeqIO.parse(f2, 'fasta'):
                if rec.id in json_data:
                    shared.append(rec.id)
                    del json_data[rec.id]
                else:
                    fa_ids.append(rec.id)
                    print(rec.id)
            print(f"Matched IDs: {len(shared)}")
            print(f"Unique IDs in fasta: {len(fa_ids)}")
            print(f"Unique IDs in json: {len(json_data)}")
            for v in json_data.values():
                print(v)
                break
            return len(shared), len(fa_ids), len(json_data)
                
        
