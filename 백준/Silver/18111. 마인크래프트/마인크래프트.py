N, M, B = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dic = {}
for lst in arr:
    for i in lst:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1

dic = sorted(dic.items())

limit = float('INF')
max_length = 0
for k in range(dic[0][0],dic[-1][0]+1):
    land_height = k
    work_time = 0
    remain_block = B
    for key, value in dic:
        if key > k:
            work_time += 2*abs(k-key)*value
            remain_block += abs(k-key)* value
        elif key< k:
            work_time += abs(k-key)*value
            remain_block -= abs(k-key)*value
    if remain_block < 0:
        continue
    if limit > work_time:
        limit = work_time
        max_length = k
    elif limit == work_time:
        max_length = max(k, max_length)
print(limit, max_length)