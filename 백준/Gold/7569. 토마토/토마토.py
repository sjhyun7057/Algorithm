'''
5 3 1  M x N, 상자의 수 H  -1은 토마토 x 0은 익지 않은거 1 은 익은 토마토
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
'''

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

di = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]
dk = [0,0,0,0,1,-1]

from collections import deque
q = deque()
# 익은 토마토 찾기
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                q.append((h,n,m))

# 퍼트리기
day = -1
while q:
    L = len(q)
    for _ in range(L):
        x, y, z = q.popleft()
        for i in range(6):
             nx = x + di[i]
             ny = y + dj[i]
             nz = z + dk[i]
             if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                 if arr[nx][ny][nz] == 0:
                     arr[nx][ny][nz] = 1
                     q.append((nx,ny,nz))
    day += 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                day = -1
print(day)