
# coding: utf-8

# # Curaxin build HiC maps

# In[1]:


#Map reads to the genome hg19 version
# In NGS we know that last nuleotide in read usually with poor quality, so we trim it from both pair mate
#See bowtie2 flags and set it based of what you want in alignment
import os
import logging
from hiclib import mapping
from mirnylib import h5dict, genome

logging.basicConfig(level=logging.DEBUG)
if not os.path.exists('/tmp'):
    os.mkdir('/tmp/') #create temp dir to store temporary alignments


# In[2]:


def HiCmapping(fastq_pathR1,outsamR1,fastq_pathR2,outsamR2):
    #R1 mapping
    mapping.iterative_mapping(
        bowtie_path='/home/msidorova/ENTER/bin/bowtie2', #path to Bowtie2
        bowtie_index_path='/tank/projects/mm_keratin_ctale/Genome/regions/Region_12/bt2_index', #path to indexed genome
        fastq_path=fastq_pathR1,
        out_sam_path=outsamR1,
        min_seq_len=25,
        len_step=5,
        seq_start=0,
        nthreads=25,  # on intel corei7 CPUs 4 threads are as fast as
                 # 8, but leave some room for you other applications
    #max_reads_per_chunk = 10000000,  #optional, on low-memory machines
        temp_dir='tmp/',  # optional, keep temporary files here
        bowtie_flags='--very-sensitive')
    print('R1_sequenses aligned')
    #R2 mapping
    mapping.iterative_mapping(
        bowtie_path='/home/msidorova/ENTER/bin/bowtie2',
        bowtie_index_path='/tank/projects/mm_keratin_ctale/Genome/regions/Region_12/bt2_index',
        fastq_path=fastq_pathR2,
        out_sam_path=outsamR2,
        min_seq_len=25,
        len_step=5,
        seq_start=0,
        nthreads=25,
    #max_reads_per_chunk = 10000000, 
        temp_dir='tmp/',
        bowtie_flags='--very-sensitive')
    print('R2_sequenses aligned')


# In[ ]:

HiCmapping('/tank/projects/mm_keratin_ctale/c_tale_hacat/raw_data/after_fastp/trimmed-I-CTRL_S4_R1_001.fastq.gz','I-CTRL_output_R1.bam','/tank/projects/mm_keratin_ctale/c_tale_hacat/raw_data/after_fastp/trimmed-I-CTRL_S4_R2_001.fastq.gz','I-CTRL_output_R2.bam')
#HiCmapping('I-HEX_S3_R1_001.fastq.gz','I-HEX_S3_R1_001.bam','I-HEX_S3_R2_001.fastq.gz','I-HEX_S3_R2_001.bam')
#HiCmapping('II-CTRL_S6_R1_001.fastq.gz','II-CTRL_S6_R1_001.bam','II-CTRL_S6_R2_001.fastq.gz','II-CTRL_S6_R2_001.bam')
#HiCmapping('II-HEX_S5_R1_001.fastq.gz','II-HEX_S5_R1_001.bam','II-HEX_S5_R2_001.fastq.gz','II-HEX_S5_R2_001.bam')


