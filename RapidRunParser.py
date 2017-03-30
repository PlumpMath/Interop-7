#!/usr/bin/python
# Class to implement the parsing of a Rapid Run

import sys 
from xml.dom import minidom
import linecache
import sys 
from rtkit.resource import RTResource
from rtkit.authenticators import QueryStringAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging

#Class that will implement parsing of Rapid Runs
class RapidRunParser():
    def __init__(self,input_file):
        self.input_file = input_file
    def test(self):
        print 'Parsing as Rapid Run'
    def collectIndex(self):
        # Return CV metrics for a rapid run here
        #print "%s" % (self.input_file)
        fileName = "/data/basemount-processing/" + self.input_file + ".index-summary.csv"
    
        try: 
            
            CV1 = linecache.getline(fileName,3).split("\t")[4]
            CV2 = linecache.getline(fileName,7).split("\t")[4]
            CVS = (0,CV1,CV2)
            """  return(CVS,PFS,Totals) """
            return(CVS)
        except:
            #print "Throwing an error"
            pass
       # return (CVS,PFS,Totals)

    def collectSummary(self):
        fileName = "/data/basemount-processing/" + self.input_file + ".summary.csv"
        
        Aligns = [0]
        Q30s = [0]
        Clusters = [0]
        Densities = [0]
        Totals = [0]
        PFs = [0]
   
        laneOffsets = [6,9]

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
