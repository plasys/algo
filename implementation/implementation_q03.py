# n, m 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, dir = map(int, input().split())
d[x][y] = 1 # 현재 시작 좌표를 방문처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향일 때 이동하게 될 x, y좌표 정의

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]

# 왼쪽으로 회전하는 함수
def turn_left():
  global dir
  dir -= 1
  if dir == -1:
    dir = 3

# 회전 시작

count = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[dir]
  ny = y + dy[dir]

  # 회전 이후 정면에 가보지 않은 칸이 존재하고 그 칸이 육지인 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    # 방문한 것으로 체크
    d[nx][ny] = 1 
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue

  # 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1

  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[dir]
    ny = y - dy[dir]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0


print(count)
    


# 좌표를 계산하는 문제는 각 방향에 대한 x좌표, y좌표 이동값에 대한 리스트를 따로 만들고, 움직일 때 해당 방향에 대한 값을 현재 좌표에 더해준다 
