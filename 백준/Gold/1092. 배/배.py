N = int(input())
crane_lst = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box_weight = sorted(list(map(int,input().split())), reverse=True)

if box_weight[0] > crane_lst[0]: 
    answer = -1
else:
    answer = 0
    while box_weight:
        for crane in crane_lst:
            if box_weight and crane < box_weight[-1]:
                continue
            for box in box_weight:
                if crane >= box:
                    box_weight.remove(box)
                    break
        answer += 1

print(answer)