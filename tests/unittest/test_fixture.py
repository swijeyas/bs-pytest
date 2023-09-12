import app.prec_calc as pcalc
import logging
import unittest as ut

class PrecCalcUT(ut.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format = '%(asctime)s %(module)s %(levelname)s: %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p', level = logging.INFO)

    # setUp and tearDown called once for each test case.
    def setUp(self):
        self.logger.info("setting up")
        self.c = pcalc.PrecCalculator()

    def tearDown(self):
        self.logger.info("tearing down")
        del self.c

    # Each test is provided a separate instance of test class.
    def test_div2(self):
        self.logger.info("use precision 2")
        self.c.set_precision(2)
        self.assertEqual(self.c.div(22, 7), 3.14)

    # "set_precision" call in "test_div2" does not affect this test case.
    def test_div_default(self):
        self.logger.info("use precision default (5)")
        self.assertEqual(self.c.div(22, 7), 3.14286)
