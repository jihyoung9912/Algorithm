class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap

    def __str__(self):
        return f"{self.elems}"

    def __setitem__(self, key, value):
        self.elems[key] = value

    def __getitem__(self, item):
        return self.elems[item]