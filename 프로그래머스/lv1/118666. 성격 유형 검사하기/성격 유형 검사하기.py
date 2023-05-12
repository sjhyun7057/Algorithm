def solution(survey, choices):
    
    ans_dict = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    for i,j in zip(survey,choices):
        if i in ans_dict.keys():
            ans_dict[i] += j-4
        else:
            ans_dict[''.join(sorted(i))] += 4-j
    
    answer = ''
    print(ans_dict)
    for k,v in ans_dict.items():
        if v>0:
            answer += k[1]
        else :
            answer += k[0] 
    
    return answer