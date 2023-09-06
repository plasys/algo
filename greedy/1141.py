n, m = map(int, input().split())

li = list(map(int, input().split()))

plusList = []
minusList = []

for i in li:
  if i > 0:
    plusList.append(i)
  else:
    minusList.append(i)

d = []
minusList.sort()

for i in range(len(minusList) // m):
  d.append(-minusList[m * i])
  
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
