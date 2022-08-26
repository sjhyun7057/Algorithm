'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

# 4 3 정상 적록 색약
'''
from pprint import pprint
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [list(input().strip()) for _ in range(n)]
color_lst = ['R', 'G', 'B']


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(root, color, weak):
    q = deque()
    q.append(root)
    if weak:
        color_dict = {'R': 'R', 'G': 'R', 'B': 'B', 0: '0'}
    else:
        color_dict = {'R': 'R', 'G': 'G', 'B': 'B', 0: '0'}
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if not visit[ni][nj] and color_dict[color] == color_dict[arr[ni][nj]]:
                    visit[ni][nj] = 1
                    q.append((ni, nj))


cnt_lst = []
for weak in range(2):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                bfs((i, j), arr[i][j], weak)
                cnt += 1
    print(cnt, end = ' ')
