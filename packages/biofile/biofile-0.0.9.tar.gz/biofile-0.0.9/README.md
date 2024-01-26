# Bioinformatics Tool: bioFile

## Introduction
Retrieve data from various file formats used in RNA-Seq data analysis. The tool currently support:
- GTF file: genomic annotations
- GFF file: genomic annoations

quick installation
```
pip install biofile
```


## Development

```
git clone git@github.com:Tiezhengyuan/bio_file.git
cd bio_file
source venv/bin/activate
```

Run unit testing:
```
pytest tests/unittests
```

## Quick tour


### Process GFF:
Retrieve annotations by features from <gff_file>. Multiple json files would be stored in <out_dir>
```
from biofile import GFF
g = GFF(gff_file, out_dir)
g.split_by_features()
```

Given an attribute, retrieve annotations from <gff_file>. and save dataframe in <out_dir>. Here, search all mRNA according to transcript_id. All related annotations are included. The output is transcript_id_mRNA.txt.
```
from biofile import GFF
g = GFF(gff_file, out_dir)
g.parse_attributes('transcript_id', 'mRNA')
```

### Process GTF:
Retrieve annotations by features from <gtf_file>. Multiple json files would be stored in <out_dir>
```
from biofile import GTF
g = GTF(gtf_file, out_dir)
g.split_by_features()
```

Given an attribute, retrieve annotations from <gtf_file>. and save dataframe in <out_dir>. Here, search all mRNA according to transcript_id. All related annotations are included. The output is transcript_id_mRNA.txt.
```
from biofile import GTF
g = GTF(gtf_file, out_dir)
g.parse_attributes('transcript_id', 'mRNA')
```



