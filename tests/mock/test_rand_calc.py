import app.rand_calc as rcalc
import random
import unittest as ut

from unittest.mock import patch

class RandCalcUT(ut.TestCase):
    def test_rand_add(self):
        rc = rcalc.RandomCalculator(1, 1000)
        # patch overwrites the target object with a Mock
        with patch("urllib.request.urlopen") as mock_open:
            # simulate public RNG with our own
            mock_request = ut.mock.Mock()
            n1 = random.randrange(1, 10)
            n2 = random.randrange(1, 10)
            mock_request.read.return_value = f"{n1}\t{n2}".encode()

            mock_open.return_value = mock_request
            
            # RandomCalculator will use our local patched object in this call
            self.assertEqual(rc.add(), n1 + n2)

        # patch restores the target object when it exits, now RandomCalculator will use public origin
        self.assertTrue(2 <= rc.add() <= 2000)
