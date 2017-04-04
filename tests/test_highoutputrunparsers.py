from unittest import TestCase
from HighOutputRunParser import HighOutputRunParser


class TestHighOutputRunParsers(TestCase):
    def setUp(self):
        self.runParser = HighOutputRunParser("./Highoutput_sample_CAPLTANXX.summary.csv")
        self.runParser.indexSummaryFile = "./Highoutput_sample_CAPLTANXX.index-summary.csv"
        self.runParser.summaryFile = "./Highoutput_sample_CAPLTANXX.summary.csv"

    def test_test(self):
        self.assertEquals(HighOutputRunParser.test(self.runParser),'Parsing as HiSeq Highoutput')

    def test_collectIndex(self):
        self.assertEquals(HighOutputRunParser.collectIndex(self.runParser),(0,'0.0008','0.0008','0.0007','0.0010','0.0014','0.0017','0.0015','0.0016')," CV Measurement is incorrect")

    def test_collectSummary(self):
        # Testing proper alignment return rate.
        self.assertEquals(HighOutputRunParser.collectSummary(self.runParser)[0],[0,"1.23","1.23","1.24","1.24","1.24","1.25","1.24","1.24"],"% Alignment stats are incorrect")
        self.assertEquals(HighOutputRunParser.collectSummary(self.runParser)[1],[0, '92.25', '92.63', '92.56', '92.64', '92.78', '92.70', '92.82', '92.99'],"% q30 stats are incorrect")
        self.assertEquals(HighOutputRunParser.collectSummary(self.runParser)[2],[0, '940', '935', '927', '923', '922', '920', '923', '924'], "Cluster Density is incorrect")
        self.assertEquals(HighOutputRunParser.collectSummary(self.runParser)[3],[0, '94.30', '94.23', '94.38', '94.42', '94.50', '94.52', '94.42', '94.48'], "% PF is incorrect")
        self.assertEquals(HighOutputRunParser.collectSummary(self.runParser)[4],[0, '261.05', '259.80', '257.60', '256.34', '256.10', '255.65', '256.53', '256.58'], "Total Reads[4] is incorrect")
        self.assertEquals(HighOutputRunParser.collectSummary(self.runParser)[5],[0, '246.12', '244.77', '243.08', '241.98', '241.95', '241.60', '242.17', '242.37'], "Reads PF[5] is incorrect")


