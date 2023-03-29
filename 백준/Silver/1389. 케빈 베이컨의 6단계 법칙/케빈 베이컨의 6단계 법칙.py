import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    lst[A].append(B); lst[B].append(A)
    

def bfs(start):
    distance = [0]*(N+1)
    visit = [0]*(N+1)
    from collections import deque 
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        j = q.popleft()
        for i in lst[j]:
            if not visit[i]:
                q.append(i)
                visit[i]=1
                distance[i] = distance[j] + 1
    
    return sum(distance)

min_tot = 100000000
idx = 0
for _ in range(1,N+1):
    tot = bfs(_)
    if min_tot > tot:
        min_tot = tot
        idx = _
print(idx)