import sys

n = int(sys.stdin.readline().rstrip())
li = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 시작시간을 기준으로 먼저 정렬 후 종료시간을 기준으로 다시 정렬한다. 
# 종료시간 오름차순으로 정렬되고, 시작시간이 같으면 역시 오름차순으로 정렬된다.
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1])

# 시작점 
right = li[0][1] # 강의 종료시간
cnt = 1

for e in li[1:]: 
  # 강의 시작시간이 기존 종료시간보다 더 크면 다음 시작점이 되고 카운트를 올림
  if e[0] >= right:
    right = e[1]
    cnt += 1

print(cnt)
