'''
1번: 한방향 1 2 3 4
2번: 양쪽 방향 1,2 3,4 그 열, 행을 전부 세보기
3번: 직각방향 1,3 2,3 1,4 2,4 네방향 모두 세보기
4번: 세방향 1,2,3 1,2,4 1,3,4 2,3,4 네 방향 모두 세보기
5번: 네방향 1,2,3,4
6번: 벽
벽은 통과 x
cctv는 서로 통과 가능

4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0

20 사각지대의 최소 크기
'''

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
cctv_spot = []
di = [[1,0], [-1,0], [0,1], [0,-1]]

lst = [[[0],[1],[2],[3]], 
       [[0,1],[2,3]], 
       [[0,2],[1,2],[0,3],[1,3]], 
       [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
       [[0,1,2,3]]]

for n in range(N):
    for m in range(M):
        if arr[n][m] in [1,2,3,4,5]:
            cctv_spot.append([n,m, arr[n][m]-1])
            

def deep_copy(arr):
    new_arr = []
    for i in arr:
        lst = []
        for j in i:
            lst.append(j)
        new_arr.append(lst)
    return new_arr

def cctv(arr, number, n, m):
    for i in number:
        dx, dy = di[i]
        nx = n
        ny = m
        while True:
            nx += dx
            ny += dy
            # 범위
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            # 벽
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = -1

def dfs(d, arr):
    global min_value
    if d == len(cctv_spot):
        cnt = 0
        for i in range(N):
            cnt += arr[i].count(0)
        min_value = min(min_value, cnt)
        return

    copy_arr = deep_copy(arr)
    x, y, cctv_num = cctv_spot[d]
    for i in lst[cctv_num]:
        cctv(copy_arr, i, x, y)
        dfs(d+1, copy_arr)
        copy_arr = deep_copy(arr)

min_value = 8*8
dfs(0, arr)
print(min_value)