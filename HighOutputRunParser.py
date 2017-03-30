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
    
    def test(self):
        print 'Parsing as HiSeq Highoutput'
    def collectIndex(self):
        fileName = "/data/basemount-processing/" + self.input_file + ".index-summary.csv"
        try:
            CV1 = linecache.getline(fileName,3).split("\t")[4]
            CV2 = linecache.getline(fileName,7).split("\t")[4]
            CV3 = linecache.getline(fileName,11).split("\t")[4]
            CV4 = linecache.getline(fileName,15).split("\t")[4]
            CV5 = linecache.getline(fileName,19).split("\t")[4]
            CV6 = linecache.getline(fileName,23).split("\t")[4]
            CV7 = linecache.getline(fileName,27).split("\t")[4]
            CV8 = linecache.getline(fileName,31).split("\t")[4]
            CVS = (0,CV1,CV2,CV3,CV4,CV5,CV6,CV7,CV8)
            """ 
            PF1 = linecache.getline(fileName,3).split("\t")[2]
            PF2 = linecache.getline(fileName,7).split("\t")[2]
            PF3 = linecache.getline(fileName,11).split("\t")[2]
            PF4 = linecache.getline(fileName,15).split("\t")[2]
            PF5 = linecache.getline(fileName,19).split("\t")[2]
            PF6 = linecache.getline(fileName,23).split("\t")[2]
            PF7 = linecache.getline(fileName,27).split("\t")[2]
            PF8 = linecache.getline(fileName,31).split("\t")[2]
            PFS = (0,PF1,PF2,PF3,PF4,PF5,PF6,PF7,PF8)

            Total1 = linecache.getline(fileName,3).split("\t")[1]
            Total2 = linecache.getline(fileName,7).split("\t")[1]
            Total3 = linecache.getline(fileName,11).split("\t")[1]
            Total4 = linecache.getline(fileName,15).split("\t")[1]
            Total5 = linecache.getline(fileName,19).split("\t")[1]
            Total6 = linecache.getline(fileName,23).split("\t")[1]
            Total7 = linecache.getline(fileName,27).split("\t")[1]
            Total8 = linecache.getline(fileName,31).split("\t")[1]
            Totals = (0,Total1,Total2,Total3,Total4,Total5,Total6,Total7,Total8)

            return(CVS,PFS,Totals)"""
            return(CVS)
        except:
            CVS = (Nan,Nan,Nan,Nan,Nan,Nan,Nan,Nan,Nan)
            """
            PFS = (0,0,0,0,0,0,0,0,0)
            Totals = (0,0,0,0,0,0,0,0,0)
            return(CVS,PFS,Totals)"""
            return(CVS)

    def collectSummary(self):
        fileName = "/data/basemount-processing/" + self.input_file + ".summary.csv"
    
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
            line = linecache.getline(fileName,i)
            Aligns.append(line.split(",")[phiXOffset].split("+")[0])
            Totals.append(line.split(",")[TotalOffset].rstrip())
            PFs.append(line.split(",")[PFOffset].rstrip())
            Q30s.append(line.split(",")[Q30Offset].rstrip())
            Densities.append(line.split(",")[DensityOffset].split("+")[0])
            Clusters.append(line.split(",")[ClusterPFOffset].split("+")[0])
    
        return(Aligns,Q30s,Clusters,Densities,Totals,PFs)
#Abstraction

