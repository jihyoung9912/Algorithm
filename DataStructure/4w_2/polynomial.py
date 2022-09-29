class Polynomial:
    """Polynomial using array."""

    def __init__(self, degree):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)

    def get_lead_exp(self):
        for i in range(self.degree, -1, -1):
            if self.coef[i] != 0:
                return i
            else:
                return "Fail"

    def evaluate(self, x):
        res = 0
        for i in range(self.degree + 1):
            if self.coef[i] != 0:
                res += self.coef[i] * x ** i
        return res


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
        ret = ""
        for coef, exp in [
            (self.coef[i], i) for i in range(self.degree + 1) if
            self.coef[i] != 0
        ][::-1]:
            ret += f"({coef})x^{exp} + "
            return f"{ret}\b\b"


if __name__ == "__main__":
    poly = Polynomial(20)
    poly.attach(3, 20).attach(2, 5).attach(4, 0)

    print(poly)
    x = 3
    res = poly.evaluate(x)
    print(f"{poly} = {res}, where x = {x}")
    print(poly.get_lead_exp())
