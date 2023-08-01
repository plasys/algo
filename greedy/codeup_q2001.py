a, b = map(int, input().split())

count = 0

# 온도 차 구하기
c = b - a
# 온도를 내리는 경우에는 부호를 반대로 해주기
if c < 0:
  c = -c
  
# 온도차를 10으로 나눈 몫을 카운트 더하기
d = c // 10
count += d

# 온도차를 10으로 나눈 나머지
e = c % 10

# 나머지가 5보다 크면
if e > 5 :
    # 나머지가 7.5 보다 크면
    if e > 7.5 :
        # 10을 한 번 더하고 1씩 빼기
        count = count + (10 - e) + 1
    # 나머지가 7.5 보다 작으면 
    else:
        # 5를 한 번 더하고 1씩 더하기
        count = count + (e - 5) + 1

# 나머지가 5보다 작으면 
elif e < 5 :
    # 나머지가 2.5 보다 크면
    if e > 2.5 :
        # 5를 한 번 더하고 1씩 빼기
        count = count + (5 - e) + 1
    else:
        # 1씩 더하기
        count = count + e

# 나머지가 5이면 
else:
    # 카운트 1 더하기
    count += 1
    
    
    
print(count)
