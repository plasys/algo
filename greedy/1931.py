import sys

n = int(sys.stdin.readline().rstrip())
li = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

li.sort(key=lambda x:(x[0], x[1]))

# 시작점 
left = li[0][0] # 강의 시작시간
right = li[0][1] # 강의 종료시간

cnt = 1
for e in li[1:]:
  # 강의 종료시간이 기존 종료시간보다 더 짧으면 시작점 변경
  if e[1] < right:
    left = e[0]
    right = e[1]
    
  # 강의 시작시간이 기존 종료시간보다 더 크면 다음 시작점이 되고 카운트를 올림
  elif e[0] >= right:
    left = e[0]
    right = e[1]
    cnt += 1

print(cnt)
