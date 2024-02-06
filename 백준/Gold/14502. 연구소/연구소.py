'''
연구소는 빈 칸, 벽으로 이루어져 있음, 벽은 칸하나를 가득 차지
벽은 꼭 3개를 세워야함
0은 빈 칸, 1은 벽, 2는 바이러스
'''

from collections import deque

N, M = map(int,input().split())
map_arr = [list(map(int,input().split())) for _ in range(N)]

di = [1,-1,0,0]; dj = [0,0,1,-1]
answer = 0
def deep_copy(arr):
    new_arr = []
    for i in arr:
        lst = []
        for j in i:
            lst.append(j)
        new_arr.append(lst)
    return new_arr

def bfs():
    global answer
    
    q = deque()
    arr = deep_copy(map_arr)
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 2:
                q.append((n,m))
    
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 2
                    q.append((ni,nj))
    
    cnt = 0 
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0:
                cnt += 1
    answer = max(answer, cnt)            
        
def dfs(k):
    if k == 3:
        bfs()
        return
    for n in range(N):
        for m in range(M):
            if map_arr[n][m] == 0:
                map_arr[n][m] = 1
                dfs(k+1)
                map_arr[n][m] = 0

dfs(0)
print(answer)
    