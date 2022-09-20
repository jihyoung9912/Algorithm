from ex03 import Element

class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap

    def __repr__(self):
        return f"Element: {self.cap}"

    def __setitem__(self, id, elem):
        self.elems[id] = elem
    def __getitem__(self, id):
        return self.elems[id]

elems = Elements()
elems[0] = Element(10)
elems[1] = Element(20)
print(elems.elems[0])
print(elems.elems[1])