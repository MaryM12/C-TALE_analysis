
# coding: utf-8

# # STEP 3

# In[1]:


#next we filter our mapped and parsed reads with collection of filters from hiclib


# In[1]:


from mirnylib import genome
from hiclib import fragmentHiC


# In[2]:


# function below perform filetring of HiC dataset and save heatmaps at selected resolutions in hdf5 and cool
def filterHiCdataset(inputhdf5,outputhdf5,enzyme,stats,outmap,resolution=[]):
    # Create a HiCdataset object.
    genome_db    = genome.Genome('Regions_hg38/', readChrms=['12_51945446-52971582','17_40495383-41581531']) #path to genome, '#' - means all number chomosomes
    fragments = fragmentHiC.HiCdataset(
        filename=outputhdf5,
        genome=genome_db,
        maximumMoleculeLength=500,
        mode='w',enzymeName=enzyme)
    # Load the parsed reads into the HiCdataset. The dangling-end filter is applied
    # at this stage, with maximumMoleculeLength specified at the initiation of the
    # object.
    fragments.parseInputData(
        dictLike=inputhdf5)
    fragments.filterRsiteStart(offset=5) #remove reads near restriction sites - 5bp
    fragments.filterDuplicates() #filter pcr duplicates
    fragments.filterLarge() #remove too large restriction fragments
    fragments.filterExtreme(cutH=0.005, cutL=0) #remove fragments with too high and low counts
    fragments.printMetadata(saveTo=stats)
    fragments._sortData() #sort data before saving map
    #fragments.saveHeatmap(filename=outmap+'_5000.hdf5',resolution=5000) #save 50kb heatmap, just first time, before
    #I full learn cooltools, this resolution is maximum without error
    for res in resolution:
        fragments.saveCooler(filename=outmap+'_'+str(res)+'hg38.cool',resolution=res)


# In[ ]:


filterHiCdataset('I-CTRL.hdf5','I-CTRL_filtered.hdf5','DpnII','I-CTRL_stats.csv','I-CTRL',resolution=[1000])
filterHiCdataset('II-CTRL.hdf5','II-CTRL_filtered.hdf5','DpnII','II-CTRL_stats.csv','II-CTRL',resolution=[1000])
filterHiCdataset('I-HEX.hdf5','I-HEX_filtered.hdf5','DpnII','I-HEX_stats.csv','I-HEX',resolution=[1000])
filterHiCdataset('II-HEX.hdf5','II-HEX_filtered.hdf5','DpnII','II-HEX_stats.csv','II-HEX',resolution=[1000])









