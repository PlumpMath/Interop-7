import sys 
from xml.dom import minidom
import linecache
import sys
import logging

#Class that will implement parsing of MiSeq runs
class MiSeqRunParser():


    def __init__(self,input_file):
        self.input_file = input_file
        self.indexSummaryFile = "/data/basemount-processing/" + self.input_file + ".index-summary.csv"
        self.summaryfile = "/data/basemount-processing/" + self.input_file + ".summary.csv"

    def test(self):
        return 'Parsing as MiSeq Run'

    def collectIndex(self):

        try:
            CV = linecache.getline(self.indexSummaryFile,3).split("\t")[4]
            CVS = (0,CV)
            return(CVS)
        except:
            pass

        #return CV,PF,Total
        #return (CVS,PFS,Totals)

    def collectSummary(self):
        rAligned = linecache.getline(self.summaryfile,6).split(",")[11]
        Aligned = rAligned.split("+")[0]
        Aligns = (0,Aligned)
        Total = linecache.getline(self.summaryfile,6).split(",")[6]
        Totals = (0,Total)
        PF = linecache.getline(self.summaryfile,6).split(",")[7]
        PFs = (0,PF)
        Q30s = (0,linecache.getline(self.summaryfile,6).split(",")[8])
        rDensity = linecache.getline(self.summaryfile,6).split(",")[3]
        rCluster = linecache.getline(self.summaryfile,6).split(",")[4]
        Cluster = rCluster.split("+")[0]
        Clusters = (0,Cluster)
        Density = rDensity.split("+")[0]
        Densities = (0,Density)

        return (Aligns,Q30s,Densities,Clusters,Totals,PFs)
