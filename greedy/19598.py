import heapq
# 강의 갯수
n = int(input())

# 강의 정보 리스트로 저장
li = [list(map(int, input().split())) for _ in range(n)]
li.sort()

# 강의 끝나는 시간을 리스트에 저장
t = []
cnt = 0

# 가장 빨리 끝나는 강의의 강의종료시간보다 시작시간이 그 이후라면 앞 강의를 pop함
# 강의종료시간을 리스트에 저장
for i in li:
  while t and t[0] <= i[0]:
    heapq.heappop(t)
  heapq.heappush(t, i[1])
  # 동시에 강의중인 수의 역대 최댓값을 cnt에 저장
  cnt = max(cnt, len(t))

print(cnt)
