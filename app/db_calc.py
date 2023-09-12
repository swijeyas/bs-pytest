import app.calc as calc
import mysql.connector

# Fetches numbers from a database and performs an arthmetic operation on them.
class DatabaseCalculator:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="devdb.lindev.local",
            user="root",
            password="r1r1r1",
            database="test"
        )
        self.c = calc.Calculator()

    def add(self):
        # fetches numbers from the database and sums them up
        total = 0
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM sum_input")

        nums = cursor.fetchmany(5)

        for n in nums:
            total = self.c.add(n[0], total)

        return total

if __name__ == "__main__":
    dbc = DatabaseCalculator()
    print(dbc.add())
