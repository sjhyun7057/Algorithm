def solution(id_list, report, k):
    
    def make_dict(id_list): # id_list에 있는 id들로 딕셔너리 만들기
        report_dict = {}
        for id in id_list:
            report_dict[id] = [0]  # 0: 신고당한 횟수
        return report_dict
    report_dict = make_dict(id_list)
    
    def make_email(report_dict, report):
        for rpt in report:
            rpt_lst = rpt.split()
            if rpt_lst[1] not in report_dict[rpt_lst[0]]: # list의 시간복잡도 O(n), Set로 바꿔서 시간복잡도가 더빠름
                report_dict[rpt_lst[0]].append(rpt_lst[1]) # 신고 한 사람의 이름을 추가
                report_dict[rpt_lst[1]][0] += 1 # 신공당했으면 1 더함
        report_lst = [] # 신고당한 id_list
        for key, value in report_dict.items():
            if value[0] >= k:
                report_lst.append(key) # 신고당한 횟수가 k보다 크면 report_lst에 추가
        email_lst = [0] * len(id_list) # 이메일 받은 횟수를 받기 위한 리스트
        idx = 0 # 인덱스 초기 값 설정
        for key, value in report_dict.items():
            
            for report_id in report_lst:
                if report_id in value:
                    email_lst[idx] += 1 # 만약 신고당한 id가 list안에 있으면 email_lst에 + 1
            idx += 1 # 인덱스 값 + 1
        return email_lst

    email_lst = make_email(report_dict, report)

    return email_lst