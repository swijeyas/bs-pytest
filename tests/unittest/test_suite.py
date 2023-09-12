import app.calc as calc
import unittest as ut

class CalcSuiteUT(ut.TestCase):
    def setUp(self):
        self.c = calc.Calculator()

    def test_add(self):
        self.assertEqual(self.c.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.c.sub(5, 10), -5)

    @ut.skip("will be fixed in next release")
    def test_mul(self):
        self.assertEqual(self.c.mul(5, 10), 50)

    def test_div(self):
        self.assertEqual(self.c.div(16, 4), 4)

    # asserts an expected exception
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.c.div(22, 0)

    # asserts a type
    def test_div_type(self):
        self.assertIs(type(self.c.div(22, 7)), float)

def sanity_suite():
    suite = ut.TestSuite()
    suite.addTest(CalcSuiteUT('test_add'))
    suite.addTest(CalcSuiteUT('test_sub'))
    suite.addTest(CalcSuiteUT('test_mul'))
    suite.addTest(CalcSuiteUT('test_div'))
    return suite

def div_suite():
    suite = ut.TestSuite()
    suite.addTest(CalcSuiteUT('test_div_zero'))
    suite.addTest(CalcSuiteUT('test_div_type'))
    return suite

runner = ut.TextTestRunner()
runner.run(sanity_suite())
runner.run(div_suite())
