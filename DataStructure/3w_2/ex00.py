SIZE = 20
arr = [i for i in range(1, SIZE + 1)]

print()
print("addr\t\tvalue")
for i in arr:
    print(id(i), i)
