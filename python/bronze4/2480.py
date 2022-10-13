num  = list(map(int, input().split()))
num.sort()
reward = 0

if num[0] == num[1] == num[2]:
  print(10000 + int(num[0]) * 1000)
elif num[0] == num[1] or num[1] == num[2]:
  print(1000 + int(num[1]) * 100)
else:
  print(int(num[2]) * 100)
