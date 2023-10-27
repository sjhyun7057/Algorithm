T = int(input())
dice_dict = {}
for i in range(1,T+1):
    dice_dict[i] = list(map(int, input().split()))

def side_number(dice_lst, idx):
    if idx == 0 or idx == 5: # a = 0, F = 5
        side_lst = dice_lst[1:5]
    elif idx == 1 or idx == 3: # B = 1 & D = 2
        side_lst = dice_lst[4:]
        side_lst.extend([dice_lst[0],dice_lst[2]])
    else: # C == 2 & E == 4
        side_lst = dice_lst[:2]
        side_lst.extend([dice_lst[3],dice_lst[5]])
    return side_lst

def find_idx(lst, num):
    for idx in range(len(lst)):
        if lst[idx] == num:
            return idx

def reverse_side(dice_lst, idx):
    if idx == 0:
        return dice_lst[5]
    elif 0 < idx < 3:
        return dice_lst[idx + 2]
    elif 3 <= idx < 5:
        return dice_lst[idx - 2]
    else:
        return dice_lst[0]

def max_number(lst):
    max_num = 0
    for i in lst:
        if i > max_num:
            max_num = i
    return max_num

def max_side_sum(side):
    tot = 0
    for lst in side:
        tot += max_number(lst)
    return tot


side_sum = []

for num in dice_dict[1]: # 첫번째 아랫면으로 올 숫자 선정
    i = 1
    idx = find_idx(dice_dict[1], num)
    side = [side_number(dice_dict[1], idx)]
    reverse_num = reverse_side(dice_dict[1], idx)
    while True:
    # 두번째
        idx = find_idx(dice_dict[i+1], reverse_num)
        side.append(side_number(dice_dict[i+1], idx))
        reverse_num = reverse_side(dice_dict[i+1], idx)
        i += 1
        if i == T:
            break
    side_sum.append(max_side_sum(side))

print(max_number(side_sum))
    

