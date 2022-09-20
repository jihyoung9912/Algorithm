class Element:
    def __init__(self, num=0):
        self.num = num

    def __str__(self):
        return f"Element:{self.num}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if not isinstance(other, Element): #other가 Element의 객체인지 확인
            raise Exception("should not be different type")
        # Element(10) + 10과 같이 Element의 class가 아닌 값을 예외처리

        add_ = self.num + other.num
        return Element(add_)

elem = Element(10) + Element(10)
print(elem)

# a = Element(10)
# print(type(a))