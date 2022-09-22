from ex03 import Element

class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.lst = [None] * cap #cap만큼의 None list 생성

    def __setitem__(self, id, value):
        self.lst[id] = value

Elements()[0] = Element(10)
print(Elements().lst[0])

# elems = Elements()
# elems[0] = Element(10)
# elems[1] = Element(20)
# print(elems.lst[0])
# print(elems.lst[1])