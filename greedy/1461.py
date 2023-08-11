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

# 몫 만큼 반복하여 묶음중 가장 큰 값을 저장
for i in range(len(minusList) // m):
  d.append(-minusList[m * i])
  
# 나머지가 있으면 나머지 묶음중 가장 절대값이 큰 값을 더해준다.
if len(minusList) % m != 0:
  d.append(-minusList[(len(minusList) // m) * m])

plusList.sort(reverse = True)
for i in range(len(plusList) // m):
  d.append(plusList[m * i])
if len(plusList) % m != 0:
  d.append(plusList[(len(plusList) // m) * m])

d.sort()
result = d.pop()
result += 2 * sum(d)
print(result)
