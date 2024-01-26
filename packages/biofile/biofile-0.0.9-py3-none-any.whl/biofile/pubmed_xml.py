"""
"""
from Bio import Entrez
from .commons import Commons

class PubmedXml(Commons):

    def __init__(self, infile:str):
        super(PubmedXml, self).__init__()
        self.infile = infile
    
    def parse_xml(self):
        fields = [
            ["PubmedArticle", "MedlineCitation", "PMID",],
            ["PubmedArticle", "MedlineCitation", "Article", "ArticleTitle"],
            ["PubmedArticle", "MedlineCitation", "Article", "Journal"],
            ['PubmedArticle', "MedlineCitation", "ChemicalList"],
        ]

        with open(self.infile, 'rb') as f:
            records = Entrez.read(f)
            # ['PubmedArticle', 'PubmedBookArticle']
            for rec in records['PubmedArticle']:
                # self.print_dict(rec["MedlineCitation"]["Article"])
                # print(rec["MedlineCitation"]["ChemicalList"])
                # print(rec["MedlineCitation"]["MeshHeadingList"])
                self.print_dict(rec['PubmedData'])
                break
        

