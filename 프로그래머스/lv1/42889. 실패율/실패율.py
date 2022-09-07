def solution(N, stages):
    length = len(stages)
    stage_dict = {}
    for s in stages:
        if s >= N+1:
            if N not in stage_dict.keys():
                stage_dict[N] = 0
            else:
                continue
        if s not in stage_dict.keys():
            stage_dict[s] = 1
        else:
            stage_dict[s] += 1
    
    failure_list = []
    stage = [i for i in range(1, N+1)]
    for i in range(1, N+1):
        failure_list.append(stage_dict.get(i,0)/length)
        length -= stage_dict.get(i,0)
        if length == 0:
            length += 1
    for i in range(N-1):
        for j in range(i,N):
            if failure_list[i] < failure_list[j]:
                failure_list[i], failure_list[j] = failure_list[j], failure_list[i]
                stage[i], stage[j] = stage[j], stage[i]
            elif failure_list[i] == failure_list[j]:
                if stage[i] > stage[j]:
                    stage[i], stage[j] = stage[j], stage[i]
    return stage
