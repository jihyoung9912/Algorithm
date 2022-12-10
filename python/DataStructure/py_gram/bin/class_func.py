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


class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap

    def __str__(self):
        return f"{self.elems}"

    def __setitem__(self, key, value):
        self.elems[key] = value

    def __getitem__(self, item):
        return self.elems[item]



elem = Element()
print(elem)
elem = Element(10)
print(elem)

elems = [Element(100), Element(200)]
print(elems)

res = Element(10) + Element(10)
print(res)

res = Element(20) - Element(10)
print(res)

elems = Elements()
elems[0] = Element(10)          # elems의 list의 값에 접근하기 위해 setitem func 필요
elems[1] = Element(20)

print(elems.elems[0])
print(elems.elems[1])

print(elems[0])                 # elems.elems로 점 연산자로 접근하지 않고, 바로 값에 접근하기 위해 getitem func 필요
print(elems[1])
print(elems)
