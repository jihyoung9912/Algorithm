N, M = map(int, input().split())

A, B, C = [], [], []

for i in range(0, N):
  A.append(list(map(int, input().split())))

for j in range(0, N):
  B.append(list(map(int, input().split())))

for i in range(len(A)):
  tmp = []
  for j in range(len(A[i])):
    tmp.append(A[i][j] + B[i][j])
  C.append(tmp)
  
for x in C:
  for y in x:
    print(y, end = ' ')
  print()