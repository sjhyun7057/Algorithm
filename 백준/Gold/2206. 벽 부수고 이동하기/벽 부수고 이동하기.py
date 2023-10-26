'''
q depth 계산하면서 하기 while q 안에 q만큼의 for문을 돌려서 길이를 depth +1 
N x M 행렬
0은 이동가능
1은 이동 불가

'''
'''
N x M 행렬
0은 이동가능
1은 이동 불가
'''

from pprint import pprint
N, M = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(N)]
visit_arr = [[0]*M for _ in range(N)]

start = (0,0,0)
def bfs(start):
    from collections import deque
    di, dj = [1,-1,0,0], [0,0,1,-1]
    q = deque()
    q.append(start)
    visit_arr[0][0] = [1,0]
    d = 0
    while q:
        d += 1
        for _ in range(len(q)):
            x, y, check = q.popleft()
            if x == N-1 and y == M-1:
                return d
            for k in range(4):
                ni = x+di[k]
                nj = y+dj[k]
                if 0<=ni<N and 0<=nj<M:
                    if not check: #그전에 벽을 통과한적이 없을 때
                        if arr[ni][nj]: # 벽을 만났을 때
                            if not visit_arr[ni][nj]:
                                visit_arr[ni][nj] = 2
                                q.append((ni,nj,1))
                        elif not arr[ni][nj]:# 길일때
                            if visit_arr[ni][nj] != 1:
                                visit_arr[ni][nj] = 1
                                q.append((ni,nj,0))
                    else: # 벽을 통과한 적이 있을 때 
                        if not arr[ni][nj]: # 길만 고려
                            if not visit_arr[ni][nj]:
                                visit_arr[ni][nj] = 2
                                q.append((ni,nj,1))
    return -1


print(bfs(start))