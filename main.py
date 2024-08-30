import math


# from Charts import *

# from scipy.stats import t

# CONST
# None

class Calculation:
    def __init__(self, h, n, r):
        self.r = r
        self.i = None
        self.n = n
        self.h = h

    def f1(self):
        self.i = (1 / self.n) * (((1 + self.n * self.r / 100) / (pow(1 + self.h / 100, self.n))) - 1)

    def f2(self):
        self.i = (self.r / 100 - self.h / 100) / (1 + self.h/100)


if __name__ == "__main__":
    r = 35
    n = 3
    h = 20

    calculation = Calculation(h, n, r)
    calculation.f1()
    print(calculation.i)
    calculation.f2()
    print(calculation.i)

    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
