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

elem = Element(10) + Element(10)