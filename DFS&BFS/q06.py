import sys

n = int(sys.stdin.readline().rstrip())
li = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

li.sort(key=lambda x:(x[0], x[1]))

left = li[0][0]
right = li[0][1]
cnt = 1
for e in li[1:]:
  
  if e[1] < right:
    left = e[0]
    right = e[1]
    
  elif e[0] >= right:
    right = e[1]
    cnt += 1

print(cnt)
