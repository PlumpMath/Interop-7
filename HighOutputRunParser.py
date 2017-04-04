import sys
from xml.dom import minidom
import linecache
import sys 
from rtkit.resource import RTResource
from rtkit.authenticators import QueryStringAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging

# Class that will eventually implement parsing of high-output runs
class HighOutputRunParser():
    
    def __init__(self,input_file):
        self.input_file = input_file
        self.indexSummaryFile = "/data/basemount-processing/" + self.input_file + ".index-summary.csv"
        self.summaryFile = "/data/basemount-processing/" + self.input_file + ".summary.csv"
    
    def test(self):
        return('Parsing as HiSeq Highoutput')

    def collectIndex(self):
        try:
            CV1 = linecache.getline(self.indexSummaryFile,3).split("\t")[4]
            CV2 = linecache.getline(self.indexSummaryFile,7).split("\t")[4]
            CV3 = linecache.getline(self.indexSummaryFile,11).split("\t")[4]
            CV4 = linecache.getline(self.indexSummaryFile,15).split("\t")[4]
            CV5 = linecache.getline(self.indexSummaryFile,19).split("\t")[4]
            CV6 = linecache.getline(self.indexSummaryFile,23).split("\t")[4]
            CV7 = linecache.getline(self.indexSummaryFile,27).split("\t")[4]
            CV8 = linecache.getline(self.indexSummaryFile,31).split("\t")[4]
            CVS = (0,CV1,CV2,CV3,CV4,CV5,CV6,CV7,CV8)

            return(CVS)
        except:
            CVS = (Nan,Nan,Nan,Nan,Nan,Nan,Nan,Nan,Nan)
            return(CVS)

    def collectSummary(self):

        Aligns = [0] 
        Q30s = [0] 
        Clusters = [0] 
        Densities = [0] 
        Totals = [0] 
        PFs = [0] 
   
        laneOffsets = [6,9,12,15,18,21,24,27]
        phiXOffset = 11
        TotalOffset = 6 
        PFOffset = 7 
        Q30Offset = 8 
        DensityOffset = 3 
        ClusterPFOffset = 4
        for i in laneOffsets:
            line = linecache.getline(self.summaryFile,i)
            Aligns.append(line.split(",")[phiXOffset].split("+")[0])
            Totals.append(line.split(",")[TotalOffset].rstrip())
            PFs.append(line.split(",")[PFOffset].rstrip())
            Q30s.append(line.split(",")[Q30Offset].rstrip())
            Densities.append(line.split(",")[DensityOffset].split("+")[0])
            Clusters.append(line.split(",")[ClusterPFOffset].split("+")[0])
    
        return(Aligns,Q30s,Densities,Clusters,Totals,PFs)
#Abstraction

