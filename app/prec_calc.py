class PrecCalculator:
    def __init__(self):
        self.p = 5

    def set_precision(self, p):
        self.p = p

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return round(a / b, self.p)

    def mul(self, a, b):
        return a / b
