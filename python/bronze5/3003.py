# found_chess = list(map(int, input().split()))
# chess = [1, 1, 2, 2, 2, 8]
# needed_chess = []

# for i in range(0, len(chess)):
#   needed_chess.append((chess[i] - found_chess[i]))
  
# print(' '.join(map(str, needed_chess)))

chess = [1, 1, 2, 2, 2, 8]

c = list(map(int, input().split()))

for i in range(6):
  print(chess[i] - c[i], end = ' ')