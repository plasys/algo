# n은 책의 갯수, m은 한 번에 들 수 있는 책의 갯수
n, m = map(int, input().split())

# 책들의 원래 위치 좌표
li = list(map(int, input().split()))

# 양수, 음수 좌표 나눠서 저장
plusList = []
minusList = []

for i in li:
  if i > 0:
    plusList.append(i)
  else:
    minusList.append(i)

d = []
minusList.sort()

# 1231231231231
