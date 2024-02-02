
N, K = map(int,input().split())
height_lst = list(map(int, input().split()))

cost_lst = []

for idx in range(N-1):
    cost_lst.append(height_lst[idx+1] - height_lst[idx])
cost_lst.sort()
print( sum(cost_lst[:N-K]))