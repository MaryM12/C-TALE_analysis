
# coding: utf-8

# # STEP 2

# In[ ]:


#Next, the output of bowtie2 have to be parsed, the separate sides of the reads combined into pairs
#and the result stored in a dict-like object.


# In[2]:


import os
import logging
from hiclib import mapping
from mirnylib import h5dict, genome


# In[1]:


def ParseMappedReads(basename1,basename2,outputh5dict,enzyme):
    mapped_reads = h5dict.h5dict(outputh5dict) #output hdf5
    genome_db    = genome.Genome('Regions_hg38/', readChrms=['12_51945446-52971582','17_40495383-41581531']) #path to genome, '#' - means all number chomosomes
    mapping.parse_sam(
        sam_basename1=basename1,
        sam_basename2=basename2,
        out_dict=mapped_reads,
        genome_db=genome_db, 
        enzyme_name=enzyme)


# In[ ]:


ParseMappedReads('I-CTRL_S4_R1_001.bam','I-CTRL_S4_R2_001.bam','I-CTRL.hdf5','DpnII')
ParseMappedReads('II-CTRL_S6_R1_001.bam','II-CTRL_S6_R2_001.bam','II-CTRL.hdf5','DpnII')
ParseMappedReads('I-HEX_S3_R1_001.bam','I-HEX_S3_R2_001.bam','I-HEX.hdf5','DpnII')
ParseMappedReads('II-HEX_S5_R1_001.bam','II-HEX_S5_R2_001.bam','II-HEX.hdf5','DpnII')








