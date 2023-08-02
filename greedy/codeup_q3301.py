# 금액 입력받기
n = int(input())

# 거스름돈 갯수
count = 0

# 거스름돈 단위
array = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in array:
    # n을 현재 단위로 나눈 몫을 카운트에 추가
    count += n // i
    # 새로운 n은 현재 단위로 나눈 나머지가 된다
    n = n % i
    
    # 나머지가 없으면 거스름돈 반환 완료
    if n == 0:
        print(count)
        break
