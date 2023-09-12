import app.calc as calc
import unittest as ut

# Must derive unittest.TestCase
class CalcUT(ut.TestCase):
    # Must prefix methods with "test"
    def test_add(self):
        c = calc.Calculator()
        self.assertEqual(c.add(2, 3), 5)

    # This test case raises uncaught DivideByZero exception.
    # PyUnit reports error separately from failure.
    # Errors prevent test case from executing.
    def test_error(self):
        c = calc.Calculator()
        self.assertEqual(c.div(5, 0), 0)

    # This test case results in failure.
    # There is a bug in "mul" method.
    def test_mul(self):
        c = calc.Calculator()
        self.assertEqual(c.mul(5, 10), 50)

    # This test case will be skipped.
    @ut.skip("will be implemented in next release")
    def test_mod(self):
        c = calc.Calculator()
        self.assertEqual(c.mod(5, 10), 5)

    def not_a_test(self):
        # Doesn't follow PyUnit naming convention for test case.
        pass
