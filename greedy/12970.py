def solution():
    n,k = map(int,input().split())

    a = 0
    b = n
    while a*b < k and b > 0:
        a += 1
        b -= 1

    if k == 0:
        return 'B'*n
    elif b == 0:
        return -1

    remain = k - (a-1)*b

    return 'A'*(a-1) + 'B'*(b-remain) + 'A' + 'B'*remain

print(solution())
