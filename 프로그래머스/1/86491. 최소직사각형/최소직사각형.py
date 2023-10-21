def solution(sizes):
    answer = 0
    first_win, second_win = [], []
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            first_win.append(i)
        elif sizes[i][0] < sizes[i][1]:
            second_win.append(i)
    if len(first_win) > len(second_win):
        for i in second_win:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    else:
        for i in first_win:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    max_width = max(sizes, key = lambda x : x[0])
    max_height = max(sizes, key = lambda x : x[1])
    
    result = max_width[0]*max_height[1]
    
    return result