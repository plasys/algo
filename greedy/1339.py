d = {}
n = int(input())
for i in range(n):
  # 자릿수 1자리 부터 시작
  x = 1
  # 입력받은 단어
  word = input()
  # 역방향부터 차례로 검사
  for n in reversed(word):
    # key에 해당 알파벳이 존재하면 기존 자릿수에 더해준다
    if n in d.keys():
      d[n] += x 
    # key에 해당 알파벳이 없으면 자릿수를 그대로 할당
    else:
      d[n] = x

    x = x * 10 # 자릿수 증가


result = 0
num = 9

# 내림차순으로 정렬 후 자릿수가 가장 큰 것부터 9 8 7... 할당
for i in sorted(list(d.values()), reverse=True):
  result = result + (num * i)
  num -= 1

print(result)
