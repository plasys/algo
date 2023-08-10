# 과제 갯수
n = int(input())

# 과제 기한, 점수를 리스트로 저장
hwList = [list(map(int, input().split())) for _ in range(n)]
# 과제 기한 기준으로 오름차순 정렬
hwList.sort()

# 해야될 숙제를 저장하는 리스트
todoList = []
result = 0
# 과제 수행 최대 날짜
k = hwList[-1][0]

for d in range(k, 0, -1):
  # 과제가 남아있고, 해당 날짜에 수행할 수 있는 과제점수를 리스트에 저장
  while hwList and hwList[-1][0] == d:
    # 그 과제를 꺼내서 점수를 저장
    todoList.append(hwList.pop()[1])

  # 수행할 수 있는 과제가 남아있으면
  if todoList:
    todoList.sort() # 오름차순 정렬
    result += todoList.pop() # 가장 큰 점수를 꺼내서 결과에 더함
    
print(result)
