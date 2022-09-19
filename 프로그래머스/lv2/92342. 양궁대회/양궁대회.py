max_score = 0
def solution(n, info):
    answer = []
    score_lst = []
    def calculate_score(lst, info):
        idx = 0
        score = 0
        for i, j in zip(lst,info):
            if i <= j and j :
                score = score - (10-idx)
            elif i > j:
                score = score + (10-idx)
            idx += 1
        return score
    def dfs(idx, n, lst):
        global max_score
        
        if idx == 11:
            if n > 0:
                lst[-1] = n
            score = calculate_score(lst, info)
            if max_score < score:
                max_score = score
                if score_lst:
                    score_lst.pop()
                score_lst.append(lst)
            elif max_score == score:
                if not max_score:
                    return 
                for i in range(len(lst))[::-1]:
                    if lst[i] > score_lst[-1][i]:
                        score_lst.pop()
                        score_lst.append(lst)
                        break
                    elif lst[i] < score_lst[-1][i]:
                        break
                # score_lst.append(lst)
            return
                
        if n - (info[idx]+1) < 0:
            dfs(idx+1, n, lst + [0])
        else:
            dfs(idx+1, n-(info[idx]+1), lst + [info[idx]+1])
            dfs(idx+1, n, lst + [0])
        
    dfs(0, n, answer)
    if max_score == 0:
        answer = [-1]
    else:
        answer = score_lst[-1]
    return answer