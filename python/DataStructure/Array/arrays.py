class Array:
    def __init__(self, cap=10):
        self.cap = cap
        self.list = [None] * cap

    def __str__(self):
        return f"{self.list}"

    def __len__(self):
        return len(self.list)

    def __setitem__(self, key, value):
        self.list[key] = value

    def __getitem__(self, item):
        return self.list[item]


if __name__ == "__main__":
    arr = Array(5)

    for i in range(len(arr)):
        arr[i] = i

    print(arr)
    index = 3
    print(f"arr[{index}] = {arr[index]}")

    for i in arr:
        print(id(i), i)

    print(sum(arr))
