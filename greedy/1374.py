import sys
import heapq
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x: x[1])

mh = []
cnt = 0

# 강의중에 가장 일찍 끝나는 시간보다 시작시간이 그 이후인 강의가 있으면 그 강의를 목록에서 뺀다.
for i in l:
    while mh and mh[0] <= i[1]: # 가장 일찍 끝나는 시간보다 시작 시간이 크면
        heapq.heappop(mh)       # mh에서 가장 작은 원소 pop & return
    heapq.heappush(mh, i[2])    # mh에 i[2]=끝나는 시간을 추가
    cnt = max(cnt, len(mh))     # 최댓값을 저장

print(cnt)
