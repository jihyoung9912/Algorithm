class Term:
    def __init__(self, coef=0, exp=0):
        self.coef = coef
        self.exp = exp

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.coef, self.exp}"


class Polynomial:
    """Polynomial using array."""

    def __init__(self):
        self.bgn = 0
        self.end = 0
        self.terms = []

    def attach(self, coef=0, exp=0):
        self.terms.append(Term(coef, exp))
        return self

    def evaluate(self, x):
        raise NotImplemented

    def find_term(self, exp) -> Optional[Term]:
        # 제공된 exp 에 상응하는 Term 을 반환한다.
        raise NotImplemented

    def __str__(self):
        ret = ""
        terms = sorted(self.terms, key=lambda x: x.exp, reverse=True)
        for i in terms:
            ret += f"({i.coef})x^{i.exp} + "
        return f"{ret}\b\b\b"
