array = ['a','b','c','d','e','f','g','h']

data = input()

x = int(array.index(data[0])) + 1
y = int(data[1])
print(x , y)
count = 0

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

for i in range(8):
  x = x + dx[i]
  y = y + dy[i]

  if x < 1 or x > 8 or y < 1 or y > 8:
    continue

  count += 1
  
print(count)


# 답안

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

if next row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
  result += 1

print(result)
