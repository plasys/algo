import math

# n은 토핑의 종류 갯수
n = int(input())

# a는 도우의 가격, b는 토핑의 가격
a, b = map(int, input().split())

# c는 도우의 칼로리
c = int(input())

# 토핑 칼로리 값 저장
d = []
for _ in range(n):
  d.append(int(input()))

# 내림차순 정렬
d.sort(reverse=True)

# 결과를 담을 리스트
array = []

# 토핑 갯수에 따라 열량/가격 값 구하기
for i in range(n):
  cal = c + sum(d[0:i])
  price = a + (b * i)
  array.append(math.floor(cal / price))

array.sort(reverse=True)
print(array[0])
