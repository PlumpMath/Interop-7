#/usr/bin/py

# This script loads metrics into RequestTracker tickets semi-automatically.
# JB and JK 01-18-17

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
        print "Needs implementation"
    def collectAlign(self):
        print "Needs implementation"

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
    parser = DataParser()
    flowcell_type = RapidRunParser()
    parser.setFlowcellType(flowcell_type)
    parser.parser_test()


