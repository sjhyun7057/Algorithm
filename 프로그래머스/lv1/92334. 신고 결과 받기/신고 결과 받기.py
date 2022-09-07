
def solution(id_list, report, k):
    
    def make_dict(id_list): # id_list에 있는 id들로 딕셔너리 만들기
        report_dict = {}
        email_idx_dict = {}
        for idx in range(len(id_list)):
            report_dict[id_list[idx]] = set()  # 0: 신고당한 횟수
            email_idx_dict[id_list[idx]] = idx
        return report_dict, email_idx_dict
    report_dict, email_idx_dict = make_dict(id_list)

    def make_email(report_dict, report):
        for rpt in report:
            rpt_lst = rpt.split()
            report_dict[rpt_lst[1]].add(rpt_lst[0]) # 신고 한 사람의 이름을 추가
        
        email_lst = [0] * len(id_list) # 이메일 받은 횟수를 받기 위한 리스트
        
        for _, value in report_dict.items():
            if len(value) >= k:
                for id in value:
                    email_lst[email_idx_dict[id]] += 1
        return email_lst

    email_lst = make_email(report_dict, report)

    return email_lst


