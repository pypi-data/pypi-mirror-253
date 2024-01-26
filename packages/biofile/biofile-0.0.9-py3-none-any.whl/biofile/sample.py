"""

"""
from biosequtils import File
from .fastq import FASTQ


class Sample:

    def read_sample_file(self, infile:str):
        '''
        Read the sample file
        '''
        sample_info={}
        #
        try: 
            in_obj = File(self.infile).readonly_handle()
            for line in in_obj:
                line=line.strip()
                sample_name, name_part, on = line.split(',')
                if on=='yes':
                    sample_info[sample_name]=name_part
            in_obj.close()
        except FileNotFoundError:
            print(self.infile, 'didnot exit!')
            pass
        #print(sample_info)
        return(sample_info)

#sample names
    def sample_info(self, dir_rawdata, file_samples, paired:bool):
        #fastq files
        R1_files, R2_files, raw_files=FASTQ.seek_fq(dir_rawdata)

        #read sample names
        sample_info=self.read_sample_file(file_samples)
        sample_names=sample_info.keys()
        #ab.basic().print_dict(sample_info)

        #sample_info                            
        sample_R1={}
        sample_R2={}
        #connect raw file to sample name
        for sample_name in sample_names:
            name_part=sample_info[sample_name]
            R1_str=','.join([ x for x in R1_files if name_part in x ])
            #print(name_part, R1_str)
            sample_R1[sample_name]=R1_str
            if paired is True:
                sample_R2[sample_name]=R1_str.replace('_R1','_R2')
        #
        #ab.basic().print_dict(sample_R1)
        #ab.basic().print_dict(sample_R2)
        return sample_R1, sample_R2