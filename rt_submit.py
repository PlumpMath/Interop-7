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

    rtnum = sys.argv[2]

    Runinfo = "/data/BaseSpace/Runs/" + file.rstrip() + "/Files/RunInfo.xml"
    xmldoc = minidom.parse(Runinfo)
    
    #get flowcell ID
    FC = xmldoc.getElementsByTagName('Flowcell')   
    FCID = FC[0].firstChild.nodeValue
    #get flowcell Date
    element = xmldoc.getElementsByTagName('Date')
    RunDate = element[0].firstChild.nodeValue

    #get RT
    """d = {}
    with open("/data/interop-github/Interop/fcid_ticket.txt") as f:
        for line in f:
            (RT,TempFCID) = line.rstrip().split("\t")
            d[TempFCID] = RT"""
           
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

      
    i = 0
    for i in range(1,int(LC)+1):
        try:
            #ignores no RT number errors
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (RunDate,runtype,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],CVS[int(i)],PFs[int(i)],Totals[int(i)])
        except:
            #ignores no RT number errors
            print "%s,%s,%s,%s,%s,%s,%s,%s,Nan,%s,%s" % (RunDate,runtype,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],PFs[int(i)],Totals[int(i)])


    set_logging('debug')
    logger = logging.getLogger('rtkit')
    resource = RTResource('http://gbcrt.ccr.buffalo.edu:8080/REST/1.0/', 'julienka', 'Northport12!', QueryStringAuthenticator)

    i = 0
    for i in range(1,int(LC)+1):
        try:
            rtnum = d[FCID]
           #print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (rtnum,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)],CVS[int(i)],PFS[int(i)],Totals[int(i)])
            content = {
                'content': {
                'CF.{Lane '+str(i)+' CV}': CVS[int(i)],
                'CF.{Lane '+str(i)+' Pass Filter}': PFs[int(i)],
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
            #print "%s\t%s\t%s\t%s\t%s\t%s\t%s\tNan\tNan\tNan" % (rtnum,FCID,i,Aligns[int(i)],Q30s[int(i)],Densities[int(i)],Clusters[int(i)])

###TODO add rdata file