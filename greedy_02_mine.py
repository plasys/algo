# 문자열 형태의 연속된 숫자(0부터 9)를 입력받고 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기 또는 더하기 연산자를 넣어 가능한 가장 큰 수를 구하는 프로그램 작성
# 연산은 왼쪽부터 순서대로 진행된다고 가정


# 수 입력받기
v = input()

# 입력받은 수를 int로 바꿔서 리스트에 저장
array = [int(i) for i in v]
result = 0

for x in array:
  # 입력받은 수가 1 이하거나, 현재 결과값이 0인 경우는 숫자를 더한다. 
  # 0이라는 숫자를 만났을 때는 곱했을 경우 0이 되어버리고, 1을 만났을 때는 곱하면 그대로이고 더해야 숫자가 커짐
  if x <= 1 or result == 0:
    result += x
  # 이외에는 곱해준다
  else:
    result *= x

# 출력
print(result)
