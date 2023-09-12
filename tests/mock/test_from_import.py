import app.rand_calc_from_import as rcalc
import random
import unittest as ut

from unittest.mock import patch

class RandCalcUT(ut.TestCase):
    # "rand_calc_from_import" uses from..import so this patch
    # does not have the expected behaviour.
    @patch("app.calc.Calculator")
    def test_add_wrong(self, mock_calc):
        n1 = 0
        n2 = 0
        def sim_add(a, b):
            print(f"sim_add with {a} and {b} called")
            nonlocal n1, n2
            n1 = a
            n2 = b
            return a + b
        rc = rcalc.RandomCalculatorFromImport(1, 100)
        mock_calc.return_value.add.side_effect = sim_add
        res = rc.add()
        self.assertEqual(res, n1 + n2)

    # "rand_calc_from_import" uses from..import so this
    # is the correct way to patch the object.
    @patch("app.rand_calc_from_import.Calculator")
    def test_add(self, mock_calc):
        n1 = 0
        n2 = 0
        def sim_add(a, b):
            print(f"sim_add with {a} and {b} called")
            nonlocal n1, n2
            n1 = a
            n2 = b
            return a + b
        rc = rcalc.RandomCalculatorFromImport(1, 100)
        mock_calc.return_value.add.side_effect = sim_add
        res = rc.add()
        self.assertEqual(res, n1 + n2)

    # Autospec restricts the Mock to mocking only
    # attributes and methods of the specified object.
    @patch("app.rand_calc_from_import.Calculator", autospec=True)
    def test_mul_spec(self, mock_calc):
        n1 = 0
        n2 = 0
        def sim_mul(a, b):
            nonlocal n1, n2
            n1 = a
            n2 = b
            return a * b
        rc = rcalc.RandomCalculatorFromImport(1, 100)
        mock_mul = mock_calc.return_value
        mock_mul.mu1.side_effect = sim_mul # there is a typo here
        res = rc.mul()
        mock_mul.assert_called()
