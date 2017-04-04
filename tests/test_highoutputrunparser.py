from unittest import TestCase
from HighOutputRunParser import HighOutputRunParser


class TestHighOutputRunParser(TestCase):
    def setUp(self):
        self.runParser = HighoutputRunParser("./Highoutput_sample_CAPLTANXX.summary.csv")
        self.runParser.indexSummaryFile = "./Highoutput_sample_CAPLTANXX.index-summary.csv"
        self.runParser.summaryfile = "./Highoutput_sample_CAPLTANXX.summary.csv"

    def test_test(self):
        self.assertEquals(RapidRunParser.test(self.runParser),'Parsing as Rapid Run')

    def test_collectIndex(self):
        self.assertEquals(RapidRunParser.collectIndex(self.runParser),(0,"0.2999","0.1278")," CV Measurement is incorrect")

    def test_collectSummary(self):
        # Testing proper alignment return rate.
        self.assertEquals(HighoutputRunParser.collectSummary(self.runParser)[0],[0,"1.94","1.62"],"% Alignment stats are incorrect")
        self.assertEquals(HighoutputRunParser.collectSummary(self.runParser)[1],[0,"98.28","98.01"],"% q30 stats are incorrect")
        self.assertEquals(HighoutputRunParser.collectSummary(self.runParser)[2], [0, "710","796"], "Cluster Density is incorrect")
        self.assertEquals(HighoutputRunParser.collectSummary(self.runParser)[3], [0, "96.31","95.40"], "% PF is incorrect")
        self.assertEquals(HighoutputRunParser.collectSummary(self.runParser)[4], [0, "130.91","146.68"], "Total Reads[4] is incorrect")
        self.assertEquals(HighoutputRunParser.collectSummary(self.runParser)[5], [0, "125.98","139.80"], "Reads PF[5] is incorrect")


