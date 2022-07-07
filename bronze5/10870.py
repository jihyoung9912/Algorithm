# def function(n):
#   if n == 0:
#     return
#   else:
#     function(n-1)
#     print(n)
    
# function(10)


num = [0, 1]
n = int(input())

for i in range(n-1):
  num.append(num[i] + num[i + 1])
print(num[n])

#피보나치 재귀함수와 tmp변수 갱신으로도 풀어볼 것