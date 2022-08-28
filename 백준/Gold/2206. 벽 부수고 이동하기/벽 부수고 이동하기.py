import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
dist_arr = [[[1000000,1000000] for i in range(M)] for _ in range(N)]
dist_arr[0][0] = [1, 1]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        i, j, cnt = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            cnt_a = 0
            if 0 <= ni < N and 0 <= nj < M:
                if cnt == 1:
                    if not arr[ni][nj] and dist_arr[ni][nj][1] > dist_arr[i][j][1] + 1:
                        dist_arr[ni][nj][1] = dist_arr[i][j][1] + 1
                        q.append((ni,nj,cnt))
                else:
                    if arr[ni][nj]:
                        cnt_a = 1
                    if dist_arr[ni][nj][cnt_a] > dist_arr[i][j][0] + 1:
                        dist_arr[ni][nj][cnt_a] = dist_arr[i][j][0] + 1
                        q.append((ni, nj, cnt_a))
    if min(dist_arr[N-1][M-1]) == 1000000:
        dist_arr[N-1][M-1] = [-1,-1]
    return dist_arr[N-1][M-1]

print(min(bfs((0,0,0))))
