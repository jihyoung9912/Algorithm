class OrderedList:
    def __init__(self):
        self.arr = []

    def __str__(self):
        return f"{self.arr}"

    def is_empty(self):
        return not bool(self.arr)

    def add(self, num):
        if not self.arr:        # self.arr이 비어있을 때, 최초에만
            self.arr.append(num)
            return
        cur = 0
        while cur < len(self) and self[cur] <= num:
            cur += 1
        self.arr.insert(cur, num)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, item):
        return self.arr[item]

    def remove(self, num):
        return self.arr.remove(num)

    def search(self, num):
        # return True if num in self.arr else False
        cur = 0
        while cur < len(self) and self[cur] != num:
            cur += 1
        return False if cur >= len(self) else True

    def index(self, num):
        return self.arr.index(num) if num in self.arr else False


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
print(o.index(43))
