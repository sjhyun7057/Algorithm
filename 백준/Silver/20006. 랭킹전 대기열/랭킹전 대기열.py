
p, m = map(int, input().split())
player_lst = [list(input().split()) for _ in range(p)]
room_lst = [[] for _ in range(300)]
limit_lst = [[] for _ in range(300)]

for lev, nam in player_lst:
    for idx in range(len(room_lst)):
        if not room_lst[idx]:
            room_lst[idx].append([int(lev), nam])
            limit_lst[idx].append(int(lev)-10)
            limit_lst[idx].append(int(lev)+10)
            break
        else:
            if limit_lst[idx][0]<=int(lev)<=limit_lst[idx][1] and len(room_lst[idx]) != m:
                room_lst[idx].append([int(lev), nam])
                break
for room in room_lst:
    if not room:
        break
    print('Started!' if len(room) == m else 'Waiting!')
    room.sort(key=lambda x : x[1])
    for r in room:
        print(*r)

