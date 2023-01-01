import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
visit = [0]*N

def check(k):
    for i in range(k):
        if visit[i] == visit[k] or abs(visit[i] - visit[k]) == k - i:
            return False
    return True

def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return

    for j in range(N):
        visit[n] = j
        if check(n):
            dfs(n+1)
    else:
        return
dfs(0)
print(cnt)