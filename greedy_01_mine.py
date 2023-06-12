# 두 수 n, k를 입력받아 n이 1이 될 때까지 두 과정중 하나를 반복적으로 선택하여 수행.
# 1) n에서 1을 뺀다.
# 2) n을 k로 나눈다. (나머지가 없을 경우에만 가능)
# 수행 횟수를 최소로 하여 구하기


import sys

# 익숙해지기 위해 라인 단위로 입력을 받아봄
data = sys.stdin.readline().rstrip()

# 입력받은 값을 공백 기준으로 나눠서 인덱스를 활용해 저장
n = int(data[0:data.index(' ')])

k = int(data[data.index(' ') + 1 : len(data)])

# 수행 횟수
count = 0

# n이 1이 될 때까지 반복
while n != 1:
  # 나머지가 없으면 나누기
  if n % k == 0:
    n //= k
    count += 1
  # 나머지가 있으면 1씩 빼기
  else:
    n -= 1
    count += 1

# 수행횟수 출력
print(count)
