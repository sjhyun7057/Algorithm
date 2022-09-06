
def solution(id_list, report, k):
    
    def make_dict(id_list):
        report_dict = {}
        # report_list = [0]*len(id_list)
        # for rpt in report:
        for id in id_list:
            report_dict[id] = [0, 0]  # 0: 신고당한 횟수, 1: 이메일 받은 횟수
        return report_dict
    report_dict = make_dict(id_list)
    
    def make_email(report_dict, report):
        for rpt in report:
            rpt_lst = rpt.split()
            if rpt_lst[1] not in report_dict[rpt_lst[0]]:
                report_dict[rpt_lst[0]].append(rpt_lst[1])
                report_dict[rpt_lst[1]][0] += 1
        report_lst = []
        for key, value in report_dict.items():
            if value[0] >= k:
                report_lst.append(key)
        email_lst = [0] * len(id_list)
        i = 0
        for key, value in report_dict.items():
            
            for report_id in report_lst:
                if report_id in value:
                    email_lst[i] += 1
            i += 1
        return email_lst

    email_lst = make_email(report_dict, report)

    return email_lst
