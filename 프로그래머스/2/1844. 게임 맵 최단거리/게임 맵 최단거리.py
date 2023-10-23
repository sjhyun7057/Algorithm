'''
캐릭터 시작위치 (0,0)
상대방 진영 (n-1, m-1)
'''
def solution(maps):
    answer = 10000
    n, m = len(maps), len(maps[0])
    start = (n-1,m-1)
    di, dj = [1,-1,0,0], [0,0,1,-1]
    visit = [[n*m+1] * m for _ in range(n)]
    from collections import deque
    q = deque()
    q.append(start)
    visit[n-1][m-1] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            # print(ni,nj)
            if 0<= ni < n and 0<= nj < m: 
                if maps[ni][nj] and visit[ni][nj] > visit[x][y] + 1:
                    q.append((ni,nj))
                    visit[ni][nj] = visit[x][y] + 1
    if visit[0][0] == n*m+1:
        return -1
    else:
        return visit[0][0]
