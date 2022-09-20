def solution(orders, course):
    from itertools import combinations

    menu_lst = []
    
    for idx in range(len(course)):
        
        menu_lst.append({})
        for order in orders:
            for i in combinations(sorted(order), course[idx]):
               menu_lst[idx][i] = menu_lst[idx].get(i, 0) + 1
        menu_lst[idx] = sorted(menu_lst[idx].items(), key = lambda x:x[1], reverse = True)

    
    answer = []
    for idx in range(len(menu_lst)):
        a = []
        for id, value in menu_lst[idx]:
            if value < 2:
                continue
            if not a:
                a.append([value,''.join(id)])
                answer.append(''.join(id))
            else:
                if value == a[0][0]:
                    answer.append(''.join(id))
    return sorted(answer)