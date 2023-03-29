def solution(fees, records):
    record_dict = {}
    for record in records:
        record_list = record.split()
        if record_list[1] not in record_dict.keys():
            record_dict[record_list[1]] = [record_list[0], 0]
        else:
            if record_dict[record_list[1]][0]:
                record_dict[record_list[1]][1] += ((int(record_list[0][:2]) - int(record_dict[record_list[1]][0][:2])) * 60 + (int(record_list[0][3:]) - int(record_dict[record_list[1]][0][3:]))) # 총 분 을 계산
                record_dict[record_list[1]][0] = 0 # 아웃된 경우 in시간 초기화
            else:
                record_dict[record_list[1]][0] = record_list[0]
    answer = []
    for key, value in sorted(record_dict.items()):
        
        if value[0]:
            value[1] += ((23 - int(value[0][:2])) * 60 + (59 - int(value[0][3:])))
            value[0] = 0
        if value[1] <= fees[0]:
            result = fees[1]
        else:
            if (value[1]-fees[0])%fees[2]: # 요금 계산
                result = fees[1] + ((value[1]-fees[0])//fees[2])*fees[3] + fees[3]
            else:
                result = fees[1] + ((value[1]-fees[0])//fees[2])*fees[3]
        answer.append(result)
    return answer