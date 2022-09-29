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

    def __add__(self, other):
        poly = Polynomial(max(self.degree, other.degree))

        while not self.is_zero() or not other.is_zero():
            exp_01 = self.get_lead_exp()
            exp_02 = other.get_lead_exp()

            if exp_01 > exp_02:
                # remove 를 적용하여야, lead_exp 의 사용이 의미가 있다.
                # remove 에 의해 특정 exp 의 coef 가 0 이 되므로
                # 이후 read_exp 시 다시 읽히는 기회가 사라진다.
                pass
            elif exp_01 < exp_02:
                pass
            else:
                pass
            return poly


if __name__ == "__main__":
    poly1 = Polynomial(20)
    poly1.attach(3, 20).attach(2, 5).attach(4, 0)
    print(poly1)

    poly2 = Polynomial(4)
    poly2.attach(1, 4).attach(10, 3).attach(3, 2).attach(1, 0)
    print(poly2)

    # poly = poly1 + poly2
    # print("poly1 + poly2 = ")
    # print(poly)
