from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j):
    q = deque()
    q.append((i, j))
    temp = [] # 인구이동을 세기위한 list
    temp.append((i, j)) # 초기좌표 추가
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(s[nx][ny] - s[x][y]) <= r: # 인구차이가 l명이상 r명 이하 그러면 국경을 염
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append((nx, ny)) # temp에 추가
    return temp
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


while True:
    visit = [[0] * n for i in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                # 만약 인구이동이 일어났으면 temp에는 2개이상의 좌표가있음
                if len(temp) > 1: # 인구이동이 일어남
                    check = True
                    num = sum([s[x][y] for x, y in temp]) // len(temp) # 연합의 인구수를 바꿈
                    # 연합의 인구수/ 연합을 이루고있는 칸의 개수
                    for x, y in temp:
                        s[x][y] = num
    if not check: # 인구이동이 일어나지 않았을 경우
        break
    cnt += 1
print(cnt)