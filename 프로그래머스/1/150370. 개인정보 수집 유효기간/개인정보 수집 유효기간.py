'''
모든 달은 28일까지
파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return
today: 오늘 날짜
terms: 약관 기간
'''
def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        category, time = term.split()
        term_dict[category] = int(time)
    privacy_lst = []
    for privacy in privacies:
        privacy_lst.append(privacy.split())
    # 뺀 기간 보다 많으면 폐기 적으면 잔류
    remain_lst = []
    idx = 1
    for lst in privacy_lst:
        remain_day = 0
        # print(today[0:4], today[5:7], today[8:10])
        if int(today[8:10]) - int(lst[0][8:10]) >= 0:
            remain_day = 1
        if (int(today[0:4])-int(lst[0][0:4]))*12 + (int(today[5:7])-int(lst[0][5:7])) + remain_day > term_dict[lst[1]]:
            answer.append(idx)
        idx += 1
    return answer