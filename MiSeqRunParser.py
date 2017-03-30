import sys 
from xml.dom import minidom
import linecache
import sys 
from rtkit.resource import RTResource
from rtkit.authenticators import QueryStringAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging

#Class that will implement parsing of MiSeq runs
class MiSeqRunParser():

    def __init__(self,input_file):
        self.input_file = input_file

    def test(self):
        print 'Parsing as MiSeq Run'

    def collectIndex(self):
        #TODO : Return CV metrics for a miseq-run here
        fileName = "/data/basemount-processing/" + self.input_file + ".index-summary.csv"
        try:
            CV = linecache.getline(fileName,3).split("\t")[4]
            CVS = (0,CV)
            return(CVS)
        except:
            pass

        #return CV,PF,Total
        #return (CVS,PFS,Totals)

    def collectSummary(self):
        fileName = "/data/basemount-processing/" + self.input_file + ".summary.csv"

        rAligned = linecache.getline(fileName,6).split(",")[11]
        Aligned = rAligned.split("+")[0]
        Aligns = (0,Aligned)
        Total = linecache.getline(fileName,6).split(",")[6]
        Totals = (0,Total)
        PF = linecache.getline(fileName,6).split(",")[7]
        PFs = (0,PF)
        Q30s = (0,linecache.getline(fileName,6).split(",")[8])
        rDensity = linecache.getline(fileName,6).split(",")[3]
        rCluster = linecache.getline(fileName,6).split(",")[4]
        Cluster = rCluster.split("+")[0]
        Clusters = (0,Cluster)
        Density = rDensity.split("+")[0]
        Densities = (0,Density)

        return (Aligns,Q30s,Densities,Clusters,Totals,PFs)
