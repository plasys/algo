# 큐 자료구조를 사용하기 위해 deque를 import
from collections import deque

# BFS 정의
def bfs(graph, start, visited):
  # 큐 초기화
  queue = deque([start])

  # 첫 시작 노드 방문 체크
  visited[start] = True
  
  # 큐가 빌 때까지 실행
  while queue:
    # 큐에서 값을 하나 꺼낸다
    v = queue.popleft()
  
    # 꺼낸 값 출력
    print(v, end = " ")
    
    # 해당 노드와 인접한 노드를 순회
    for i in graph[v]:
      # 방문한 적이 없으면
      if not visited[i]:
        # 큐에 추가
        queue.append(i)
        # 방문 처리
        visited[i] = True
        
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
bfs(graph, 1, visited)
