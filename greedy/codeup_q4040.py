# n은 성수기 총 기간, m은 방의 갯수
n, m = map(int, input().split())

# i + 1일차의 예약 상태 저장
array = []

for i in range(n):
  array.append(input())

# s는 도착날, t는 떠나는 날
s, t = map(int, input().split())

# 방을 옮기는 최소 횟수
def m1(array):
  result = 0
  # 'O인' 인덱스를 저장해두는 배열
  arr = []
  # 도착날부터 떠나는 날 전날까지 탐색
  for a in array[(s-1):(t-1)]:
    # 만약 'O'가 없으면 예약 불가능이므로 -1 반환
    if a.find('O') == -1:
      result = -1
      return result

    # arr이 비어있을 경우 'O'인 인덱스들을 첫 저장
    if len(arr) == 0:
      # 문자열 탐색
      for i in range(len(a)):
        # 'O' 이면 인덱스를 저장
        if a[i] == 'O':
          arr.append(i)

    else:
      # 'O'인 인덱스들 검사
      for j in arr:
        # 이전 'O'와 이어지면 그대로 두기
        if a[j] == 'O':
          pass
        # 'X'면 해당 인덱스 삭제
        else:
          arr.remove(j)

      # 검사 후 비어있으면 다른 'O'의 인덱스를 찾아 채워넣기
      if len(arr) == 0:
        for i in range(len(a)):
          # 'O' 이면 인덱스를 저장
          if a[i] == 'O':
            arr.append(i)

        # 방을 교체했으므로 횟수 추가
        result += 1

  return result

print(m1(array))
