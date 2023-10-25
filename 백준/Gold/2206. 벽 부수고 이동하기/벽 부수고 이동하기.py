'''
N x M 행렬
0은 이동가능
1은 이동 불가

'''
from pprint import pprint
N, M = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(N)]
visit_arr = [[[N*M + 1, N*M + 1]]*M for _ in range(N)]

di, dj = [1,-1,0,0], [0,0,1,-1]

start = [(N-1,M-1),0]
from collections import deque
q = deque()
q.append(start)
visit_arr[N-1][M-1] = [1,1]

while q:
    # print(q)
    dot, crush = q.popleft()
    x, y = dot
    # pprint(visit_arr)
    for k in range(4):
        
        ni = x+di[k]
        nj = y+dj[k]
        if 0<=ni<N and 0<=nj<M:
            if crush:
                if not arr[ni][nj] and visit_arr[ni][nj][1] > visit_arr[x][y][1] + 1:
                    visit_arr[ni][nj] = [visit_arr[ni][nj][0], visit_arr[x][y][1] + 1]
                    q.append([(ni,nj),crush])
            else:
                if arr[ni][nj]:
                    visit_arr[ni][nj] = [visit_arr[ni][nj][0], visit_arr[x][y][0] + 1]
                    q.append([(ni,nj),1])
                else:
                    if visit_arr[ni][nj][0] > visit_arr[x][y][0] + 1:
                        visit_arr[ni][nj] = [visit_arr[x][y][0] + 1,visit_arr[ni][nj][1]]
                        q.append([(ni,nj),0])

if visit_arr[0][0][0] == N * M +1 and visit_arr[0][0][1] == N*M + 1:
    print(-1)
else:
    print(min(visit_arr[0][0]))