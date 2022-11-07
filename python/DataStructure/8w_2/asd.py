k = int(input("입력: "))

# for i in range(1, k+1):
#     for j in range(1 + i+1):
#         print(i, end=" ")
#         i += k + 1
#     print()

for i in range(1, k + 1):
    for j in range(1, i+1):
        print(i, end = " ")
    print()