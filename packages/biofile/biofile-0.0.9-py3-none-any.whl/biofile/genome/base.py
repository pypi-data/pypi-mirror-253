

class Base:
    def __init__(self, local_files:str, outdir:str) -> None:
        self.local_files = local_files
        self.outdir = outdir

    def get_infile(self, pattern:str):
        for file in self.local_files:
            if file.endswith(pattern):
                return file
        return None