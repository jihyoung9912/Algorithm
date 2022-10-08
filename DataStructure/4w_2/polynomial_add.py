class Polynomial:
    """Polynomial using array."""

    def __init__(self, degree):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)

    def get_lead_exp(self):
        for i in range(self.degree, -2, -1):
            if self.coef[i] != 0:
                return i
            elif i <= -1:
                raise Exception("Failed to get_lead_exp")

    def evaluate(self, x):
        sum_ = 0
        for i in range(0, self.degree + 1):
            if self.coef[i] != 0:
                sum_ += x ** i * self.coef[i]
        return sum_

    def get_coef(self, exp):
        return self.coef[exp]

    def is_zero(self):
        return not any(self.coef)

    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0

    def attach(self, coef, exp):
        self.coef[exp] = coef
        return self

    def remove(self, exp):
        self.coef[exp] = 0

    def __str__(self):
        poly = ''
        for i in range(self.degree, -1, -1):
            if self.coef[i] != 0:
                poly += str(f"({self.coef[i]})x^{i} + ")
        return poly + "\b\b"

    def __add__(self, other):
        poly = Polynomial(max(self.degree, other.degree))
        while not self.is_zero() or not other.is_zero():
            exp_01 = self.get_lead_exp()
            exp_02 = other.get_lead_exp()

            if exp_01 > exp_02:
                poly.attach(self.get_coef(exp_01), exp_01)
                self.remove(exp_01)
            elif exp_01 < exp_02:
                poly.attach(other.get_coef(exp_02), exp_02)
                other.remove(exp_02)
            else:
                coef = self.get_coef(exp_01) + other.get_coef(exp_02)
                exp = exp_01
                poly.attach(coef, exp)

                self.remove(exp_01)
                other.remove(exp_02)

        return poly


if __name__ == "__main__":
    poly1 = Polynomial(20)
    poly1.attach(3, 20).attach(2, 5).attach(4, 0)
    print(poly1)
    poly2 = Polynomial(4)
    poly2.attach(1, 4).attach(10, 3).attach(3, 2).attach(1, 0)
    print(poly2)
    poly = poly1 + poly2
    print("poly1 + poly2 = ")
    print(poly)