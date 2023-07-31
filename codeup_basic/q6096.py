array = []

# 19 * 19 인 바둑판에 돌을 놓는다
for i in range(19):
    array.append(list(map(int, input().split())))

# 시작점 좌표의 갯수
n = int(input())

# 2개의 좌표에 영향을 받는 돌들의 색을 변환
for i in range(n):
    x, y = map(int, input().split())
    
    # 세로 축의 값을 변환
    for j in range(len(array)):
        if array[j][y-1] == 0:
            array[j][y-1] = 1
        else:
            array[j][y-1] = 0
            
    # 가로 축의 값을 변환
    for k in range(len(array[0])):
        if array[x-1][k] == 0:
            array[x-1][k] = 1
        else:
            array[x-1][k] = 0


# 결과를 출력
for i in range(len(array)):
    for j in range(len(array[0])):
        print(array[i][j], end = " ")
    print()
