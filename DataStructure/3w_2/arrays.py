class Array():
    def __init__(self, len=10):
        self.len = len
        self.arr = [i for i in range(self.len)]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __getitem__(self, item):
        return self.arr[item]

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        return str(self.arr)


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
