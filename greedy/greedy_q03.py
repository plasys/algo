n, m = list(map(int, input().split()))

array = []

for i in range(n):
  # 각 행의 요소들을 list에 담아 정렬하고 가장 작은 수를 따로 배열에 추가함.
  a = list(map(int, input().split()))
  a.sort(reverse=True)
  array.append(a[m-1])

# 배열을 다시 정렬하여 가장 뒤에 있는 숫자를 출력함.
array.sort()
print(array[len(array)-1])





# 모범 답안. min 함수를 사용함. 
n, m = list(map(int, input().split()))

result = 0
for i in range(n):
  a = list(map(int, input().split()))
  min_value = min(a)
  result = max(result, min_value)

print(result)
