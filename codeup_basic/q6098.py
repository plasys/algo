# 미로 생성
array = []

# 미로 초기화
for i in range(10):
  array.append(list(map(int, input().split())))

# 첫 시작점은 (2,2) 이고 9로 표시
x = 1
y = 1
array[x][y] = 9

# 개미가 움직이는 두 방향(우, 하)의 x좌표, y좌표 정의
dx = [0, 1]
dy = [1, 0]

while True:
  # 우로 이동
  nx = x + dx[0] 
  ny = y + dy[0]
  
  # 벽을 만났으면
  if array[nx][ny] == 1:
    # 하로 이동
    nx = x + dx[1]
    ny = y + dy[1]

    # 하로 이동했는데도 벽을 만났으면 멈춤
    if array[nx][ny] == 1:
      break

    # 하로 이동해서 먹이를 만났을 경우 멈춤
    elif array[nx][ny] == 2:
      # 이동한 곳을 9로 표시
      array[nx][ny] = 9
      break
      
    # 최종적으로 x와 y 값을 확정 변경
    x = nx
    y = ny
    # 이동한 곳을 9로 표시
    array[x][y] = 9

  # 벽을 안 만났으면
  elif array[nx][ny] == 0:
    x = nx
    y = ny
    # 이동한 곳을 9로 표시
    array[x][y] = 9

  # 먹이를 만났을 경우
  elif array[nx][ny] == 2:
    x = nx
    y = ny
    # 이동한 곳을 9로 표시
    array[x][y] = 9
    break


for i in range(len(array)):
  for j in range(len(array[i])):
    print(array[i][j], end = " ")

  print()
