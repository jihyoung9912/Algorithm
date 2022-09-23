from ex03 import Element

class Elements:
    def __init__(self, num = 10):
        self.num = num
        self.lst = [None] * num

    def __setitem__(self, id, value):
        self.lst[id] = value



elems = Elements()
elems[0] = Element(10)
elems[1] = Element(20)
print(elems.lst[0])
print(elems.lst[1])