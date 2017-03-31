from unittest import TestCase
from MiSeqRunParser import MiSeqRunParser


class TestMiSeqRunParser(TestCase):
    def setUp(self):
        self.runParser = MiSeqRunParser("./AYDCE_RT988_10pM_20PCTof10pM_LD.summary.csv")
        self.runParser.indexSummaryFile = "./AYDCE_RT988_10pM_20PCTof10pM_LD.index-summary.csv"
        self.runParser.summaryfile = "./AYDCE_RT988_10pM_20PCTof10pM_LD.summary.csv"

    def test_test(self):
        #self.assertEquals(MiSeqRunParser,"A")
        pass
        #self.assertEquals(test (),'Parsing as MiSeq Run')

    def test_collectIndex(self):
        #self.assertEquals(MiSeqRunParser(self.indexSummaryFile),"Test")
        pass##self.fail()

    def test_collectSummary(self):
        # Testing proper alignment return rate.
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[0],(0,"23.16"),"% Alignment stats are incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[1],(0,"87.15"),"% q30 stats are incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[2], (0, "570"), "Cluster Density is incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[3], (0, "93.48"), "% PF is incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[4], (0, "14.70"), "[4] is incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[5], (0, "13.75"), "[5] is incorrect")

        #self.assertEquals(self.runParser.collectSummary(self.runParser)[0], "Test")


if __name__ == '__main__':
    unittest.main()