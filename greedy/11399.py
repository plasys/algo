# 사람 수
n = int(input())

# 각자 걸리는 시간을 list에 저장
li = list(map(int, input().split()))

# 오름차순 정렬
li.sort()

result = 0
sum = 0
for i in li:
  result += i
  sum += result

print(sum)
