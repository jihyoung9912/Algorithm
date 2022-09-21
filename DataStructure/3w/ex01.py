class Element:
    def __init__(self, num = 0):
        self.num = num
    def __str__(self):
        return f'Element : {self.num}'
    def __repr__(self):
        return str(self)

elem = [Element(100), Element(10)]
print(elem)