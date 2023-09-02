import sys

n = int(sys.stdin.readline().rstrip())
li = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

li.sort(key=lambda x:(x[0], x[1]))

left = li[0][0]
right = li[0][1]
cnt = 1
for e in li[1:]:
  # 강의 종료시간이 짧으면 시작점 변경
  if e[1] < right:
    left = e[0]
    right = e[1]
    
  # 강의 시작시간이 종료시간보다 크면 다음 시작점이 됨 
  elif e[0] >= right:
    right = e[1]
    cnt += 1

print(cnt)

# 123123123123123123123123123123123123123123123123123
