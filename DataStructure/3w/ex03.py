class Element:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return f"Element:{self.num}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if not isinstance(other, Element):
            raise Exception("should not be different type")

        add_ = self.num + other.num
        return Element(add_)

    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception("should not be different type")

        sub = self.num - other.num
        return Element(sub)

# elem = Element(55) - Element(10)
# print(elem)