import app.calc as calc
import pytest

# Must prefix functions with "test"
def test_calc():
    c = calc.Calculator()
    assert c != None

# Must prefix classes with "Test"
class TestCalcUT():
    # Must prefix methods with "test"
    def test_add(self):
        c = calc.Calculator()
        assert c.add(2, 3) == 5

    # This test case raises uncaught DivideByZero exception.
    def test_error(self):
        c = calc.Calculator()
        assert c.div(5, 0) == 0

    # This test case results in failure.
    # There is a bug in "mul" method.
    def test_mul(self):
        c = calc.Calculator()
        assert c.mul(5, 10) == 50, "5 x 10 must be 50"

    # This test case will be skipped.
    @pytest.mark.skip(reason="will be implemented in next release")
    def test_mod(self):
        c = calc.Calculator()
        assert c.mod(5, 10), 5

    def not_a_test(self):
        # Doesn't follow PyTest naming convention for test case.
        pass

# Tests can be marked for introspection by other tests
# or for executing marked tests.
@pytest.mark.div
class TestMarker():
    def test_dev(self):
        c = calc.Calculator()
        assert c.div(5, 1) == 5

class testNotATest():
    # Doesn't follow PyTest naming convention for test case.
    def test_test(self):
        pass

