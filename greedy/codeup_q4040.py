# n은 성수기 총 기간, m은 방의 갯수
n, m = int(input().split())

# i + 1일차의 예약 상태 저장
array = []

for i in range(n):
  array.append(input())

s, t = int(input().split())

# 방을 옮기는 최소 횟수
def m1(array):
  result = 0
  arr = []
  for a in array:
    idx = a.find('O')
    # 만약 O가 없으면 예약 불가능이므로 -1 반환
    if idx == -1:
      result = -1
      return result

    # 첫 번째 O의 인덱스 저장
    arr.append(idx)
    
    while idx != a.rfind('O'):
      arr.append(idx)
      # 
      idx = a.find('O', idx, len(a))
