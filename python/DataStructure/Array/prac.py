numbers = []

while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

index = int(input())
criterion = int(input())

if index < 0 or index >= len(numbers):
    print("Not in range")
else:
    result = [num for num in numbers[:index] if num > criterion]
    for num in result:
        print(num)

numbers = []

# Accept numbers until 0 is entered
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

# Input the index and reference number
index = int(input("Enter an index: "))
ref_number = int(input("Enter a reference number: "))

# Check if the index is out of range
if index >= len(numbers):
    print("Not in range")
elif index < numbers.index(ref_number):
    print("Not in range")
else:
    result = [num for num in numbers[:index] if num > criterion]
    for num in result:
        print(num)