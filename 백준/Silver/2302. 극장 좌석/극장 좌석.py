'''
0 = 1
1 = 1
2 = 2
3 = 3
4 = 5
5 = 8
'''

N = int(input()) # 좌석개수
M = int(input()) # vip수
for _ in range(0):
    print(1)
if M:
    vip_seat = list(int(input()) for _ in range(M))

def check_batch(n):
    lst = [1, 1]
    if n == 0 or n == 1:
        return 1
    for i in range(2, n):
        lst.append(lst[i-1] + lst[i-2])
    return lst

lst = check_batch(N+1)
batch_lst = []
idx = 1
if M:
    for vip in vip_seat:
        batch_lst.append(vip-idx)
        idx = vip + 1
    if N+1 - idx:
        batch_lst.append(N+1-idx)

    tot_batch = 1
    for batch in batch_lst:
        tot_batch *= lst[batch]
else:
    tot_batch = lst[N]
    
print(tot_batch)
        