class OrderedList:
    def __init__(self):
        self.elems = []
    def is_empty(self):
        return not bool(self.elems)
    def add(self, elem):
        if not self.elems:
            self.elems.append(elem)
            return
        cur = 0
        while cur < len(self) and self[cur] <= elem:
            cur += 1
        self.elems.insert(cur, elem)
    def remove(self, elem):
        self.elems.remove(elem)
    def search(self, elem):
        cur = 0
        while cur < len(self) and self[cur] != elem:
            cur += 1
        return False if cur >= len(self) else True