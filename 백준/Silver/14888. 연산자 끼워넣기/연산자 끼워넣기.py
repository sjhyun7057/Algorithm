'''
2
5 6
0 0 1 0
'''
import sys
input = sys.stdin.readline

N = int(input())
number_lst = list(map(int, input().split()))
pmmd_lst = list(map(int, input().split()))

min_sum = float('inf')
max_sum = -float('inf')

def dfs(i, tot, p, m, x, d):
    global max_sum, min_sum
    if i >= N-1:
        max_sum = max(max_sum, tot)
        min_sum = min(min_sum, tot)
        return
    if p:
        dfs(i+1, tot+number_lst[i+1], p-1, m, x, d)
    if m:
        dfs(i+1, tot-number_lst[i+1], p, m-1, x, d)
    if x:
        dfs(i+1, tot*number_lst[i+1], p, m, x-1, d)
    if d:
        dfs(i+1, int(tot/number_lst[i+1]), p, m, x, d-1)

dfs(0, number_lst[0], pmmd_lst[0], pmmd_lst[1], pmmd_lst[2], pmmd_lst[3])
print(max_sum)
print(min_sum)