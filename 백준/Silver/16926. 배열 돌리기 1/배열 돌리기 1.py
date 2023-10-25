'''
바깥쪽부터 차근차근 시계반대방향으로 돔

'''

N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

arr_lst = [[] for _ in range(min(N,M)//2)]
empty_lst = [[0]*M for _ in range(N)]
cnt = min(N, M)
min_i = 0; i = N
min_j = 0; j = M
idx = 0
while cnt:
    n_lst = [min_i, i]
    m_lst = [min_j,j]
    for x in range(min_j, j):
        arr_lst[idx].append(arr[n_lst[0]][x])
    for y in range(min_i+1,i-1):
        arr_lst[idx].append(arr[y][m_lst[1]-1])
    for x in range(j-1, min_j-1, -1):
        arr_lst[idx].append(arr[n_lst[1]-1][x])
    for y in range(i-2,min_i,-1):
        arr_lst[idx].append(arr[y][m_lst[0]])
    min_i, i = min_i + 1, i - 1
    min_j, j = min_j + 1, j - 1
    cnt -= 2
    idx += 1
# print(arr_lst)
for i in range(len(arr_lst)):
    K = R % len(arr_lst[i])
    arr_lst[i] = arr_lst[i][K:] + arr_lst[i][:K]
# print(arr_lst)
start_i, start_j = -1, -1
finish_i, finish_j = N, M
for lst in arr_lst:
    start_i, start_j = start_i + 1, start_j + 1
    finish_i, finish_j = finish_i - 1, finish_j - 1
    i, j = start_i, start_j
    for k in range(len(lst)):
        empty_lst[i][j] = lst[k]
        if i == start_i and j != finish_j:
            j += 1
        elif j == finish_j and i != finish_i:
            i += 1
        elif j != start_j and i == finish_i:
            j -= 1
        else:
            i -= 1


for _ in empty_lst:
    print(*_)

