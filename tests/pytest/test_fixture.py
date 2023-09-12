import app.prec_calc as pcalc
import app.calc as calc
import logging
import os
import pytest

logger = logging.getLogger(__name__)
logging.basicConfig(format = '%(asctime)s %(module)s %(levelname)s: %(message)s',
                datefmt = '%m/%d/%Y %I:%M:%S %p', level = logging.INFO)

# Can be a setup and teardown using "yield" (or finalizers)
@pytest.fixture(scope="function")
def calculator():
    logger.info("setting up")
    yield pcalc.PrecCalculator()
    logger.info("tearing down")

# Can be chained with other Fixtures
@pytest.fixture
def calculator3(calculator):
    calculator.set_precision(3)
    return calculator

# Can use multiple Fixtures in the same test.
# Same Fixture can be used in multiple tests.
@pytest.fixture
def calculator_with_precision(calculator, request):
    precision = getattr(request.instance, "precision", 5)
    calculator.set_precision(precision)
    return calculator

# Can be parameterized, test cases are not aware of the parameterization.
@pytest.fixture(params=[pcalc.PrecCalculator, calc.Calculator], ids=["Precision", "Basic"])
def calculator_type(request):
    c = request.param()
    return c

class TestPrecCalcUT():
    precision = 4

    # requests a basic Fixture
    def test_div2(self, calculator):
        logger.info("use precision 2")
        calculator.set_precision(2)
        assert calculator.div(22, 7) == 3.14

    # request has chained and multiple Fixtures
    def test_div3(self, calculator3):
        logger.info("use precision 3")
        assert calculator3.div(22, 7) == 3.143

    # uses a Fixture which introspects the caller (queries "precision" attribute)
    def test_precision(self, calculator_with_precision):
        logger.info("use precision 4")
        assert calculator_with_precision.div(22, 7) == 3.1429

    # uses parameterized Fixture, test case is not aware of parameterization.
    def test_type(self, calculator_type):
        assert calculator_type.div(22, 2) == 11

    # same Fixture is used in "test_div2" but doesn't affect this test case
    def test_div_default(self, calculator):
        logger.info("use precision default (5)")
        assert calculator.div(22, 7) == 3.14286

    # uses Fixture defined in conftest.py which is autouse type
    # so it doesn't have to be requested explicitly.
    def test_confpy(self, calculator):
        logger.info(f"using UT framework - {os.environ['UT_FRAMEWORK']}")
        calculator.set_precision(2)
        assert calculator.div(22, 7) == 3.14
