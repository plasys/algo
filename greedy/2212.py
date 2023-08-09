import sys

def myFunc():
  # 센서의 갯수
  n = int(sys.stdin.readline().rstrip())
  
  # 집중국의 갯수
  k = int(sys.stdin.readline().rstrip())

  # 집중국의 갯수가 센서의 갯수와 같거나 크면 수신가능 영역의 길이는 0이 된다.
  if(k >= n):
    return 0
    
  # 센서의 좌표를 list에 저장
  arr = list(map(int, sys.stdin.readline().rstrip().split()))
  arr.sort()
  
  arr2 = []
  
  # 인접한 좌표간의 거리차이를 구해서 새로운 list에 저장
  for i in range(n - 1):
    arr2.append(arr[i + 1] - arr[i])
  
  arr2.sort()

  # n개의 좌표들의 인접한 거리의 갯수는 n-1 이고 k개의 집중국을 설치하면 k-1개의 인접한 거리를 없애준다.
  # 그림을 그려서 생각해보는 것도 좋다. 집중국을 설치하는 의미는 인접한 거리들중 가장 멀리 떨어진 거리(비효율적인 거리)를 없애줄 수 있다는 것
  # 따라서 (n - 1) - (k - 1) = n - k가 되고, 오름차순으로 정렬했을 때 뒤쪽에 있는 비효율적인 거리를 제외한 거리들을 앞에서부터 더해주면 된다.
  result = sum(arr2[:(n - k)])

  return result
  
print(myFunc())
