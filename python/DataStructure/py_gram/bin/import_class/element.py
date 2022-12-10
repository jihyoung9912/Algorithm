class Element:
    def __init__(self, elem=0):
        self.elem = elem

    def __str__(self):
        return f"Element: {self.elem}"

    def __repr__(self):
        return str(self)
        # return self.__str__과 무슨 차이?

    def __add__(self, other):
        if not isinstance(other, Element):
            raise Exception("should not be different type")  # other이 Element class가 아닌 경우 예외처리

        return self.elem + other.elem

    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception("should not be different type")

        return self.elem - other.elem
