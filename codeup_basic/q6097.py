# 세로(h), 가로(w)
h, w = map(int, input().split())

# 격자판 생성
array = [[0] * w for _ in range(h)]

# 막대의 갯수
n = int(input())

for i in range(n):
    # 막대의 길이(l), 막대의 방향(d), 막대의 좌표 x(세로), y(가로)
    l, d, x, y = map(int, input().split())
    
    # 만약 방향이 가로면
    if d == 0:
        for j in range(y, y + l):
            array[x - 1][j - 1] = 1
            
    # 만약 방향이 세로면
    elif d == 1:
        for k in range(x, x + l):
            array[k - 1][y - 1] = 1


# 막대를 놓은 후 격자판 출력
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = " ")
    print()
