'''
주식 하나를 산다.
원하는 만큼 가지고 있는 주식을 판다.
아무것도 안한다.
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
0
10
5
'''

T = int(input())

for tc in range(T):
    N= int(input())
    day_profit = list(map(int, input().split()))
    tot_profit = 0
    max_profit = day_profit[-1]
    for n in range(N-2,-1,-1):
        if day_profit[n] > max_profit:
            max_profit = day_profit[n]
        else:
            tot_profit += (max_profit - day_profit[n])
            
    print(tot_profit)