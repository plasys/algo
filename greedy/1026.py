# 숫자 개수
n = int(input())

# 내림차순 정렬
a = list(map(int, input().split()))
a.sort(reverse=True)

# 오름차순 정렬
b = list(map(int, input().split()))
b.sort()

sum = 0
for i in range(n):
  sum += (a[i] * b[i])

# 최솟값 출력
print(sum)
