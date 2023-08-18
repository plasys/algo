N = int(input())    # 사과나무의 개수
 
h = list(map(int, input().split())) # 나무의 높이
 
cnt = 0
if sum(h) % 3 == 0:
    for i in h:
        cnt += i // 2
    if cnt >= (sum(h) / 3):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
