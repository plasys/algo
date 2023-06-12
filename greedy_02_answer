data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)


# 내 풀이와의 차이점 : int값으로 변환하느라 반복문을 한 번 더 사용했음. 시간복잡도가 불필요하게 늘어남.
