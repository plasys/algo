# n은 동전의 종류, k는 목표 금액
n, k = map(int, input().split())

li = []
# 각 동전의 가치 저장
for _ in range(n):
  li.append(int(input()))

# 동전 갯수 카운트
count = 0

while True:
  # 몫을 카운트에 더한다
  count += (k // li[n-1])
  # 나머지
  remain = k % li[n-1]
  # 나머지가 0이면 다 나눈거니까 종료
  if remain == 0:
    break
  
  # 나머지가 0이 아니면 나머지는 새로운 k가 된다.
  else:
    k = remain
    # n을 1씩 줄여나감
    n = n - 1

print(count)
