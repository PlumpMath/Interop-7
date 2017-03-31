#!/usr/bin/python

# This script loads metrics into RequestTracker tickets semi-automatically.
# JB and JK 01-18-17

import sys
from xml.dom import minidom
import linecache
from rtkit.resource import RTResource
from rtkit.authenticators import QueryStringAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging
from RapidRunParser import RapidRunParser
from MiSeqRunParser import MiSeqRunParser
from HighOutputRunParser import HighOutputRunParser
import matplotlib
import numpy as np
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#Abstraction
class DataParser:
    def __init__(self,input_file):
        self.input_file = input_file
    def setFlowcellType(self, flowcell_obj):
        self.flowcell_obj = flowcell_obj
    def parser_test(self):
        self.flowcell_obj.test()
    def collectIndex(self):
        return self.flowcell_obj.collectIndex()
    def collectSummary(self):
        return self.flowcell_obj.collectSummary()
    
# Main Method
if __name__ == '__main__':

    file = sys.argv[1]
    #Set up our abstract parsing object which will later be assigned to a flowcell parsing strategy
    parser = DataParser(file)

    # Capture the directory from the command line

    #rtnum = sys.argv[2]

    Runinfo = "/data/BaseSpace/Runs/" + file.rstrip() + "/Files/RunInfo.xml"
    xmldoc = minidom.parse(Runinfo)
    
    #get flowcell ID
    FC = xmldoc.getElementsByTagName('Flowcell')   
    FCID = FC[0].firstChild.nodeValue
    #get flowcell Date
    element = xmldoc.getElementsByTagName('Date')
    RunDate = element[0].firstChild.nodeValue

    #get RT
    d = {}
    with open("/data/interop-github/Interop/fcid_ticket.txt") as f:
        for line in f:
            (RT,TempFCID) = line.rstrip().split("\t")
            d[TempFCID] = RT
           
    #get specs of each type of sequencing run
    element = xmldoc.getElementsByTagName('FlowcellLayout')
    LC = (element[0].attributes['LaneCount'].value)
    SC = (element[0].attributes['SurfaceCount'].value)

    flowcell_type = 0
    runtype = ""
    if( LC=="8"):
        flowcell_type = HighOutputRunParser(file)
        runtype = "High-Output"
    elif(LC=="2"):
        flowcell_type = RapidRunParser(file)    
        runtype = "Rapid"
    elif(LC=="1" and SC =="2"):
        flowcell_type = MiSeqRunParser(file)
        FCID = FCID.split("-")[1]
        runtype = "Miseq"
    elif(LC =="1" and SC =="1"):
        flowcell_type = MiSeqRunParser(file)
        FCID = FCID.split("-")[1]
        runtype = "Nano"
    
    parser.setFlowcellType(flowcell_type)

    #Make sure we are using the right parsing strategy
    #parser.parser_test()

    #Collect the indexing information (CV, Total Reads, Cluster PF) 
    try:
        (CVS) = parser.collectIndex()
    except:
        pass#print "We failed to collect the CV, PFS and Total metrics"
 
    #Collect the summary stats for each lane
    (Aligns,Q30s,Densities,Clusters,Totals,PFs)  = parser.collectSummary()
  
    ##plotter

    """ Laner = range(1,int(LC)+1)
    gth = np.arange(int(LC))
    Alignment = np.array(Aligns[1:]).astype(np.float)
    Q30 = np.array(Q30s[1:]).astype(np.float)
    Density = np.array(Densities[1:]).astype(np.float)
    Cluster = np.array(Clusters[1:]).astype(np.float)
    Pass = np.array(PFs[1:]).astype(np.float)
    Total = np.array(Totals[1:]).astype(np.float)
    ##pdf generation
    with PdfPages(FCID+".pdf")as pdf: 
        grid_size = (6,2)
        #alignment 
        plt.subplot2grid(grid_size,(1,0), rowspan=2, colspan =1)
        plt.bar(gth,Alignment)
        plt.ylabel('Percent')
        plt.xticks(gth,Laner)
        plt.yticks(np.arange(0,2,.2))
        plt.plot((-1,2),(0.8,0.8),'k--')
        plt.plot((-1,2),(1.2,1.2), 'k--')
        plt.title('Alignment')
        #Q30
        plt.subplot2grid(grid_size,(1,1), rowspan=2, colspan =1)
        plt.bar(gth,Q30)
        plt.ylabel('Percent')
        plt.xticks(gth,Laner)
        plt.yticks(np.arange(0,101,20))
        plt.title('Q30')
        #Density
        plt.subplot2grid(grid_size,(3,0), rowspan=2, colspan =1)
        plt.bar(gth,Density)
        plt.ylabel('Percent')
        plt.xticks(gth,Laner)
        plt.yticks(np.arange(0,101,20))
        plt.title('Clusters Pass Filter')
        #Cluster
        plt.subplot2grid(grid_size, (3,1),rowspan=2, colspan =1)
        plt.bar(gth,Cluster)
        plt.ylabel('K/mm^2')
        plt.xticks(gth,Laner)
        plt.title('Cluster Density')
        plt.yticks(np.arange(0,1200,200))
        plt.tight_layout()
        pdf.savefig()
        plt.close()"""
      
    i = 0    
    for i in range(1,int(LC)+1):
        try:
            
            #ignores no RT number errors
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (RunDate,runtype,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],CVS[int(i)],PFs[int(i)],Totals[int(i)])
          #print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (RunDate,runtype,d[FCID],FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],CVS[int(i)],PFS[int(i)],Totals[int(i)])
        except:
            
            #ignores no RT number errors
            print "%s,%s,%s,%s,%s,%s,%s,%s,Nan,%s,%s" % (RunDate,runtype,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],PFs[int(i)],Totals[int(i)])
            #print "%s,%s,%s,%s,%s,%s,%s,%s,%s,Nan,Nan,Nan" % (RunDate,runtype,d[FCID],FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)])





    ###plotter
    #data_to_plot = [Aligns,Q30s,Densities,Clusters,PFs,Totals]
    #print(data_to_plot)
    #fig = plt.figure(1, figsize=(9,6))
    #ax = fig.add_subplot(111)
    #box = ax.boxplot(np.array(data_to_plot).astype(np.float))
    #fig.savefig('fig1.png', bbox_inches='tight')





## Start of RT logging, leave commented off please
"""
    set_logging('debug')
    logger = logging.getLogger('rtkit')
    resource = RTResource('http://gbcrt.ccr.buffalo.edu:8080/REST/1.0/', 'julienka', 'Northport12!', QueryStringAuthenticator)
    
    i = 0
    for i in range(1,int(LC)+1):
        try:
            rtnum = d[FCID]
            print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (rtnum,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],CVS[int(i)],PFS[int(i)],Totals[int(i)])
            content = {
                'content': {
                'CF.{Lane '+str(i)+' CV}': CVS[int(i)],
                'CF.{Lane '+str(i)+' Pass Filter}': PFS[int(i)],
                'CF.{Lane '+str(i)+' Cluster Density}': Clusters[int(i)]      
                } 
            }
            try:
                response = resource.post(path='ticket/' + rtnum + '/edit', payload=content,)
                logger.info(response.parsed)
            except RTResourceError as e:
                logger.error(e.response.status_int)
                logger.error(e.response.status)
                logger.error(e.response.parsed)

        except:
            print "%s\t%s\t%s\t%s\t%s\t%s\t%s\tNan\tNan\tNan" % (rtnum,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)])

"""
