


def solution(brown, yellow):
    answer = []
    block = brown + yellow
    wh_lst = []
    for i in range(2, int(block**(1/2)) + 1):
        if block % i == 0:
            wh_lst.append([block//i, i])
    
    yellow_lst = []
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            yellow_lst.append([yellow//i, i])
            
    for yellow in yellow_lst:
        for brown in wh_lst:
            if brown[0] > yellow[0] and brown[1] > yellow[1]:
                if brown[0] - 2 == yellow [0] and brown[1] - 2 == yellow[1]:
                    return brown