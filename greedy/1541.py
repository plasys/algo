# 입력받은 문자열
s = input()

# -로 자르기
li1 = list(s.split("-"))

# 자른 문자열들을 계산한 결과를 담는 리스트
li2 = []

# 각각의 문자열 계산
for e in li1:
  li2.append(sum(map(int, e.split("+"))))

# 결과값
fv = 0

# 첫 번째 값은 양수, 그 뒤에 값들은 마이너스
for e in range(len(li2)):
  if e != 0:
    fv -= li2[e]
  else:
    fv += li2[e]

print(fv)
