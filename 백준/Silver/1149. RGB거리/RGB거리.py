'''
RGB거리에는 집이 N개 
집은 빨 초 파 중 하나 색 
N번집의 색은 N-1번, N+1번 색과 같지 않아야함
'''
import sys
input = sys.stdin.readline
N = int(input())
color_cost = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    color_cost[i][0] = min(color_cost[i-1][1], color_cost[i-1][2]) + color_cost[i][0]
    color_cost[i][1] = min(color_cost[i-1][0], color_cost[i-1][2]) + color_cost[i][1]
    color_cost[i][2] = min(color_cost[i-1][1], color_cost[i-1][0]) + color_cost[i][2]
    
    
print(min(color_cost[N-1]))