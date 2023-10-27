N = int(input())
length = int(input())
recommend_lst = list(map(int, input().split()))
cnt_dict = {}
for i in range(length):
    if len(cnt_dict) < N:
        if recommend_lst[i] not in cnt_dict.keys():
            cnt_dict[recommend_lst[i]] = [1,i]
        else:
            cnt_dict[recommend_lst[i]][0] += 1
    else:
        if recommend_lst[i] not in cnt_dict.keys():
            lst = sorted(cnt_dict.items(), key = lambda x : [x[1][0], x[1][1]])
            cnt_dict.pop(lst[0][0],None)
            cnt_dict[recommend_lst[i]] = [1,i]
        else:
            cnt_dict[recommend_lst[i]][0] += 1

print(*sorted(cnt_dict.keys()))