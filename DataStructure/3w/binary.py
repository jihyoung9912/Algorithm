class Binary():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return ''.join(str(i) for i in data)

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        self.data = self.data[::-1]
        other.data = other.data[::-1]
        add_bin = [0 for i in range(max(len(self.data), len(other.data)))]
        carry = 0

        for i in range(min(len(self.data), len(other.data))):
            if self.data[i] == 0 and other.data[i] == 0:
                if carry == 1:
                    carry = 0
                    add_bin[i] = 1
                else:
                    carry = 0
                    add_bin[i] = 0

            elif (self.data[i] == 1 and other.data[i] == 0) or (other.data[i] == 1 and self.data[i] == 0):
                if carry == 1:
                    add_bin[i] = 0
                    carry = 1
                else:
                    carry = 0
                    add_bin[i] = 1

            elif self.data[i] == 1 and other.data[i] == 1:
                if carry == 1:
                    add_bin[i] = 1
                    carry = 1
                else:
                    carry = 1
                    add_bin[i] = 0

        tmp = 1
        if len(self.data) < len(other.data):
            tmp = 0

        if tmp == 1:
            for i in range(min(len(self.data), len(other.data)), max(len(self.data), len(other.data))):
                if self.data[i] == 0 and carry == 0:
                    carry = 0
                    add_bin[i] = 1

                elif (self.data[i] == 1 and carry == 0) or (carry == 1 and self.data[i] == 0):
                    if carry == 1:
                        add_bin[i] = 1
                        carry = 0
                    else:
                        carry = 0
                        add_bin[i] = 1

                elif self.data[i] == 1 and carry == 1:
                    add_bin[i] = 0
                    carry = 1

        else:
            for i in range(min(len(self.data), len(other.data)), max(len(self.data), len(other.data))):
                if carry == 0 and other.data[i] == 0:
                    carry = 0
                    add_bin[i] = 1

                elif (carry == 1 and other.data[i] == 0) or (other.data[i] == 1 and carry == 0):
                    if carry == 1:
                        add_bin[i] = 1
                        carry = 0
                    else:
                        carry = 0
                        add_bin[i] = 1

                elif carry == 1 and other.data[i] == 1:
                    add_bin[i] = 0
                    carry = 1
        if carry == 1:
            add_bin.append(1)
        add_list = add_bin[:: -1]
        return ''.join(str(i) for i in add_list)


*data, = "110101011"
*data, = map(int, data)
b1 = Binary(data)
print(b1)  # 110101011
print(len(b1))

*data, = "110111"
*data, = map(int, data)
b2 = Binary(data)
print(b2)
print(len(b2))

b = b1 + b2
print(b)