
def solution(survey, choices):
    kakao_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    for i in range(len(survey)):
        if choices[i] > 4:
            kakao_dict[survey[i][-1]] += score_dict[choices[i]]
        elif choices[i] < 4:
            kakao_dict[survey[i][0]] += score_dict[choices[i]]
    
    kakao_key = list(kakao_dict.keys())
    kakao_value = list(kakao_dict.values())
    kakao_result = ''
    for i in range(0, 8, 2):
        if kakao_value[i] >= kakao_value[i+1]:
            kakao_result += kakao_key[i]
        else:
            kakao_result += kakao_key[i+1]
    return kakao_result