n, m, k = list(map(int, input().split()))

array = list(map(int, input().split()))
array.sort()

# 배열의 크기 n

# 숫자 더하는 횟수 m

# 최대 연속으로 더할 수 있는 횟수 k
# K <= M 이다.

print(n, m, k)



# 1. 정렬 후 가장 큰 수와 두 번째로 큰 수를 찾는다.
a = array[n-1] # 첫 번째로 큰 수
b = array[n-2] # 두 번째로 큰 수

# 2. M을 (K+1)로 나눈 몫과 나머지를 구한다.
c = m / (k + 1) # 몫
d = m % (k + 1) # 나머지

print(a, b , c , d)

# 3. (몫 * (k * a + b)) + (나머지 * a)
print(c * (k * a + b) + (d * a))
