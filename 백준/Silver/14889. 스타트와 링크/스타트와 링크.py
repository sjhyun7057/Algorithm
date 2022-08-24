'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
import sys
input = sys.stdin.readline


def sum_startlink(lst):
    tot = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            tot += arr[lst[i]][lst[j]]
    return tot

def dfs(i,start,link):
    global min_balance
    if len(start) > N/2 or len(link) > N/2:
        return
    if i == N:
        start_sum = sum_startlink(start)
        link_sum = sum_startlink(link)
        min_balance = min(abs(start_sum-link_sum), min_balance)

    dfs(i+1, start+[i], link)
    dfs(i+1, start, link+[i])


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
min_balance = sum(map(sum, arr))
dfs(0, [], [])
print(min_balance)