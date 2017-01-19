#/usr/bin/py

# This script loads metrics into RequestTracker tickets semi-automatically.
# JB and JK 01-18-17

import sys
from xml.dom import minidom

#Class that will implement parsing of Rapid Runs
class RapidRunParser():
    def __init__(self):
        pass
    def test(self):
        print 'Parsing as Rapid Run'
    def collectCV(self):
	#TODO : Return CV metrics for a rapid run here
        print "Needs implementation"
    def collectAlign(self):
        print "Needs implementation"

#Class that will implement parsing of MiSeq runs
class MiSeqRunParser():
    def __init__(self):
        pass
    def test(self):
        print 'Parsing as MiSeq Run'
    def collectCV(self):
	#TODO : Return CV metrics for a miseq-run here
        print "MiSeq -- Needs implementation"
    def collectAlign(self):
        print "MiSeq -- Needs implementation"

# Class that will eventually implement parsing of high-output runs
class HighOutputRunParser():
    def __init__(self):
        pass
    def test(self):
        print 'Parsing as HiSeq Highoutput'
    def collectCV(self):
	#TODO : Return CV metrics for a high-output run here
        print "Needs implementation"
    def collectAlign(self):
        print "Needs implementation"

#Abstraction
class DataParser:
    def __init__(self):
        pass
    def setFlowcellType(self, flowcell_obj):
        self.flowcell_obj = flowcell_obj
    def parser_test(self):
        self.flowcell_obj.test()
    def collectCV(self):
        self.flowcell_obj.collectCV()
    def collectAlign(self):
        self.flowcell_obj.collectAlign()


# Main Method
if __name__ == '__main__':

    #Set up our abstract parsing object which will later be assigned to a flowcell parsing strategy
    parser = DataParser()

    # Capture the directory from the command line

    file = sys.argv[1]
    found = file.rstrip() + '/Files/RunInfo.xml'#Parameters.xml'
    xmldoc = minidom.parse(found)
    element = xmldoc.getElementsByTagName('FlowcellLayout')

    LC = (element[0].attributes['LaneCount'].value)
    SC = (element[0].attributes['SurfaceCount'].value)
    flowcell_type = 0
    if( LC=="8"):
        flowcell_type = HighOutputRunParser()
    elif(LC=="2"):
        flowcell_type = RapidRunParser()    
    elif(LC=="1" and SC =="2"):
        flowcell_type = MiSeqRunParser()
    elif(LC =="1" and SC =="1"):
        flowcell_type = MiSeqRunParser()

    parser.setFlowcellType(flowcell_type)
    parser.parser_test()
    parser.collectCV()
    parser.collectAlign()



