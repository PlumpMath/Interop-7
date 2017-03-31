from unittest import TestCase
from MiSeqRunParser import MiSeqRunParser


class TestMiSeqRunParser(TestCase):
    def setUp(self):
        self.runParser = MiSeqRunParser("./MiSeq_sample_RT988.summary.csv")
        self.runParser.indexSummaryFile = "./MiSeq_sample_RT988.index-summary.csv"
        self.runParser.summaryfile = "./MiSeq_sample_RT988.summary.csv"

    def test_test(self):
        self.assertEquals(MiSeqRunParser.test(self.runParser),'Parsing as MiSeq Run')

    def test_collectIndex(self):
        # Tests the return of correct Lane CV
        self.assertEquals(MiSeqRunParser.collectIndex(self.runParser),(0,"1.0148")," CV Measurement is incorrect")

    def test_collectSummary(self):
        # Testing proper alignment return rate.
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[0],(0,"23.16"),"% Alignment stats are incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[1],(0,"87.15"),"% q30 stats are incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[2], (0, "570"), "Cluster Density is incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[3], (0, "93.48"), "% PF is incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[4], (0, "14.70"), "Total Reads[4] is incorrect")
        self.assertEquals(MiSeqRunParser.collectSummary(self.runParser)[5], (0, "13.75"), "Reads PF[5] is incorrect")

