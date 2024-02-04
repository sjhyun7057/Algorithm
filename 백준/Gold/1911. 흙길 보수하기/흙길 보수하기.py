N, L = map(int, input().split())#웅덩이, 널빤지 길이

pool_lst = [list(map(int, input().split())) for _ in range(N)] # (시작위치, 끝위치)

pool_lst.sort(key=lambda x : x[0])

idx = pool_lst[-1][-1] + 1
cnt = 0

while pool_lst:
    start, end = pool_lst.pop()
    if idx < end:
        if (idx-start) % L:
            k = (idx - start)//L + 1
        else:
            k = (idx-start)//L
    else:
        idx = end
        if  (idx-start) % L:
            k = (idx - start)//L + 1
        else:
            k = (idx-start)//L
    cnt += k
    idx -= (L*k)
print(cnt)