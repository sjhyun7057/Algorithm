N, M, start = map(int, input().split())


lst = [[] for _ in range(N)]



dfs_visit = [0]*N
bfs_visit = [0]*N
for _ in range(M):
    n, m = map(int, input().split())
    lst[n-1].append(m)
    lst[m-1].append(n)


for i in lst:
    i.sort()

dfs_visit[start-1] = 1
bfs_visit[start-1] = 1

dfs_lst = [start]
bfs_lst = [start]


def dfs(start):
    
    for i in lst[start-1]:
        if not dfs_visit[i-1]:
            dfs_visit[i-1] = 1
            dfs_lst.append(i)
            dfs(i)
dfs(start)
print(*dfs_lst)


def bfs(start):
    from collections import deque 
    q = deque()
    q.append(start)
    while q:
        i = q.popleft()
        for j in lst[i-1]:
            if not bfs_visit[j-1]:
                q.append(j)
                bfs_lst.append(j)
                bfs_visit[j-1] = 1
                
bfs(start)
print(*bfs_lst)