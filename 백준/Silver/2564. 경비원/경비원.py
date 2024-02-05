'''
10 5
3
1 4
3 2
2 8
2 3
'''
N, M = map(int, input().split())
store = int(input())

spot_lst = [list(map(int, input().split())) for _ in range(store)] # 1 북, 2 남, 3 서, 4 동 
# 북이나 남일 경우 왼쪽 경계로 부터의 거리, 동이나 서일 경우 위쪽 경계로부터 거리
my_spot, my_distance = list(map(int,input().split()))


tot_distance = 0
for spot, distance in spot_lst:
    if my_spot == spot:
        tot_distance += abs(distance-my_distance)
    else:
        if my_spot == 1:
            if spot == 2:
                tot_distance += min((my_distance + M + distance), (N-my_distance + M + N-distance))
            elif spot == 3:
                tot_distance += my_distance + distance
            else:
                tot_distance += (N-my_distance + distance)
        elif my_spot == 2:
            if spot == 1:
                tot_distance += min((my_distance + M + distance), (2*N - my_distance + M -distance))
            elif spot == 3:
                tot_distance += my_distance + M - distance
            else:
                tot_distance += N - my_distance + M - distance
        elif my_spot == 3:
            if spot == 1:
                tot_distance += my_distance + distance
            elif spot == 2:
                tot_distance += M-my_distance + distance
            else:
                tot_distance += min((my_distance + N + distance), (2*M - my_distance + N - distance))
        else:
            if spot == 1:
                tot_distance += my_distance + N - distance
            elif spot == 2:
                tot_distance += my_distance + distance
            else:
                tot_distance += min((my_distance + N + distance), (2*M - my_distance + N - distance))
print(tot_distance)