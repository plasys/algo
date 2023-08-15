# n은 유치원생의 수, k는 조의 갯수
n, k = map(int, input().split())

# 유치원생들의 키를 저장
li = list(map(int, input().split()))

# 인접한 유치원생들의 키 차이를 저장
d = []

for i in range(n - 1):
  d.append(li[i + 1] - li[i])

d.sort()

# 조를 나눈다는 의미 = 인접한 원생들 키 차이중 가장 큰 값부터 (k - 1) 개만큼 차례로 없애는 것.
result = sum(d[:(n - 1) - (k - 1)])

print(result)
