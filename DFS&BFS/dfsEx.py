# dfs 정의
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  # 방문한 노드 값 출력
  print(v, end = " ")

  # 인접한 노드에 대해 
  for i in graph[v]:
    # 방문한 적이 없으면 재귀적으로 방문
    if not visited[i]:
      dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
