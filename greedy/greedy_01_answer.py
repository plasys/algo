n, k = map(int, input().split())

result = 0

while True:2
  target = (n // k) * k
  result += (n - target)
  n = target

  # n이 k보다 작아져서 더 이상 나눌 수 없을 때 반복문 탈출
  if n < k:
    break
  # k로 나누기
  n //= k
  result += 1
  
# 마지막으로 남은 수에 대하여 1씩 뺀 횟수를 계산하여 더해준다.
result += (n - 1)
print(result)



# 내 풀이와의 차이점 : 1을 빼는 과정이 다르다. 한 번에 가능한 만큼 여러번 1을 빼고 나서 나눗셈을 실행하고, 마지막에도 1을 한 번에 빼서 실행횟수를 줄였음.
