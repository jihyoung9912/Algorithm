class Binary:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        ans = ''
        for i in self.data:
            ans += str(i)
        return ans

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __add__(self, other):
        if not isinstance(other, Binary):
            raise Exception("Please add Binary type")

        if len(self.data) > len(other.data):
            return self.bin(self.data, other.data)
        else:
            return self.bin(other.data, self.data)

    def bin(self, first_bin, second_bin):

        ans = ""
        carry = 0

        while second_bin:
            if carry == 0:
                num = first_bin.pop() + second_bin.pop()
            else:
                num = first_bin.pop() + second_bin.pop() + 1
                carry -= 1
            if num == 3:
                carry += 1
                ans = "1" + ans
            elif num == 2:
                carry += 1
                ans = "0" + ans
            elif num == 1:
                ans = "1" + ans
            elif num == 0:
                ans = "0" + ans

        while first_bin:
            if carry == 1:
                num = first_bin.pop() + 1
                carry -= 1
            else:
                num = first_bin.pop()
            if num == 3:
                carry += 1
                ans = "1" + ans
            elif num == 2:
                carry += 1
                ans = "0" + ans
            elif num == 1:
                ans = "1" + ans
            elif num == 0:
                ans = "0" + ans
        if carry == 1:
            ans = "1" + ans

        return ans


*data, = "110101011"
*data, = map(int, data)
b1 = Binary(data)
print(b1)  # 110101011
print(len(b1))  # 9

*data, = "110111"
*data, = map(int, data)
b2 = Binary(data)
print(b2)  # 110111
print(len(b2))  # 6

b = b1 + b2
print(b)  # 111100010
print(len(b))  # 9
print(b[4]) # 0
