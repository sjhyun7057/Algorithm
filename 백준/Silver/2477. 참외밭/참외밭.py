'''
동쪽 1 서쪽 2 남쪽 3 북쪽 4
'''

K = int(input())
cham_lst = [list(map(int,input().split())) for _ in range(6)] # 방향과 길이

weight_point = [[1,0],[-1,0],[0,-1],[0,1]] # 동 서 남 북
start = (0,0)

way_lst = [start]

for way, length in cham_lst:
    w_x, w_y = weight_point[way-1]
    x, y = way_lst[-1]
    x += length * w_x
    y += length * w_y
    way_lst.append((x,y))


max_x = max(way_lst, key= lambda x : x[0])
max_y = max(way_lst, key= lambda x : x[1])
min_x = min(way_lst, key= lambda x : x[0])
min_y = min(way_lst, key= lambda x : x[1])
max_place = (max_x[0]-min_x[0]) * (max_y[1]-min_y[1])
max_dot = [(max_x[0],min_y[1]),(max_x[0],max_y[1]),(min_x[0],min_y[1]),(min_x[0],max_y[1])]

bot_lst = []
for dot in max_dot:
    if dot not in way_lst:
        bot_lst.append(dot)

empty_p_x = 0
empty_p_y = 0
for way in way_lst:
    if min_x[0]<way[0]<max_x[0]:
        empty_p_x = way[0]
    if min_y[1]<way[1]<max_y[1]:
        empty_p_y = way[1]
    if empty_p_x and empty_p_y:
        break
empty_place = abs((bot_lst[0][0]-empty_p_x)*(bot_lst[0][1]-empty_p_y))
print((max_place - empty_place)*K)