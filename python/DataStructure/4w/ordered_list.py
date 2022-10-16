class OrderedList:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return not bool(self.elems)

    def __str__(self):
        return f"{self.elems}"

    def add(self, elem):
        cur = 0

        while cur < len(self) and self[cur] <= elem:
            cur += 1

        self.elems.insert(cur, elem)

    def __len__(self):
        return len(self.elems)

    def __getitem__(self, item):
        return self.elems[item]

    def remove(self, elem):
        self.elems.remove(elem)

    def search(self, elem):
        # return True if elem in self.elems else False
        cur = 0
        while cur < len(self.elems) and self.elems[cur] != elem:
            cur += 1
        return False if cur >= len(self.elems) else True

    def index(self, elem):
        cur = 0
        while cur < len(self.elems) and self.elems[cur] != elem:
            cur +=1
        return cur if cur < len(self.elems) else "Not in list"

*data, = 53, 17, 34, 23, 15, 43
print(data)
o = OrderedList()
print(o.is_empty())
for i in data:
    o.add(i)
print(o.is_empty())
print(o)
o.remove(23)
print(o)
print(o.search(53))
print(o.index(53))