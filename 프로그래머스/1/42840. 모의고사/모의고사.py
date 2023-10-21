'''
1,2,3,4,5, 1,2,3,4,5

2,1,2,3,2,4,2,5, 
3,3,1,1,2,2,4,4,5,5
'''

def solution(answers):
    first = [1,2,3,4,5] * 2000 + [0]
    second = [2,1,2,3,2,4,2,5] * 1250 + [0]
    third = [3,3,1,1,2,2,4,4,5,5] * 1000 + [0]
    
    for idx in range(len(answers)):
        if answers[idx] == first[idx]:
            first[-1] += 1
        if answers[idx] == second[idx]:
            second[-1] += 1
        if answers[idx] == third[idx]:
            third[-1] += 1
    
    lst = [first[-1], second[-1], third[-1]]
    
    max_answer = max(lst)
    result = []
    for i in range(len(lst)):
        if max_answer == lst[i]:
            result.append(i+1)
        
    
    return result