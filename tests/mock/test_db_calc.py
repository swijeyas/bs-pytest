import app.db_calc as dbcalc
import random
import unittest as ut

from unittest.mock import patch

total = 0
def generate(*args):
    global total
    randoms = []
    print(f"generate {args[0]} random numbers")
    for i in range(args[0]):
        n = random.randrange(1, 100)
        randoms.append((n,))
        total += n

    # mock_tuples = ut.mock.Mock() will throw an exception
    # use MagicMock to easily mock magic methods.
    mock_tuples = ut.mock.MagicMock()
    mock_tuples.__iter__.return_value = randoms

    return mock_tuples

class DbCalcUT(ut.TestCase):
    # patch can be done with decorator or context manager
    @patch("mysql.connector.connect")
    def test_db_add(self, mock_connect):
        global total
        total = 0

        mock_db = mock_connect.return_value
        mock_cursor = mock_db.cursor.return_value

        # side_effect will be called when caller calls fetchmany
        # side_effect return overrides return value of return_value attribute
        mock_cursor.fetchmany.side_effect = generate

        dbc = dbcalc.DatabaseCalculator()
        
        self.assertEqual(dbc.add(), total)

        # We can assert if mock methods were called or not called, or called specific number of times, or with certain arguments
        mock_connect.assert_called_once_with(host='devdb.lindev.local', user='root', password='r1r1r1', database='test')
        mock_db.commit.assert_not_called()
        mock_cursor.execute.assert_called_once_with('SELECT * FROM sum_input')
        mock_cursor.fetchmany.assert_called_once_with(5)
