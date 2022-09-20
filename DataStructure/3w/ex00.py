class Element:
    def __init__(self, num=0): #defauklt argument, parameter
        self.num = num

    def __str__(self):
        return f"Element:{self.num}"

elem = Element()
print(elem)
elem = Element(10)
print(elem)