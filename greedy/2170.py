import sys
# 선 갯수
n = int(sys.stdin.readline())

# 튜플로 저장(list로 했더니 시간초과됨, tuple이 저장 속도 및 인덱싱 속도가 더 빠르다.)
li = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
li.sort()

left = li[0][0]
right = li[0][1]

result = 0

# 새로운 선분의 시작점, 끝점 위치에 따라 right, left를 수정
for i in li[1:]:
  if i[1] <= right:
    continue
  elif i[0] <= right < i[1]:
    right = i[1]
  elif right < i[0]:
    result += right - left
    left = i[0]
    right = i[1]

result += right - left
print(result)
