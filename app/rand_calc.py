import app.calc as calc
import urllib.request

# Fetches two random numbers from a public origin and performs an arthmetic operation on them.
class RandomCalculator:
    def __init__(self, start, end):
        self.url = "https://www.random.org/integers/?num=2&min={}&max={}&col=2&base=10&format=plain&rnd=new".format(start, end)
        self.c = calc.Calculator()

    def add(self):
        # returns two random decimal integers between start-end, separated by TAB
        r = urllib.request.urlopen(self.url)

        nums = r.read().decode().split("\t")

        print(f"adding {nums[0]} and {nums[1]}")
        return self.c.add(int(nums[0]), int(nums[1]))

    def mul(self):
        r = urllib.request.urlopen(self.url)

        nums = r.read().decode().split("\t")

        return self.c.div(int(nums[0]), int(nums[1]))
