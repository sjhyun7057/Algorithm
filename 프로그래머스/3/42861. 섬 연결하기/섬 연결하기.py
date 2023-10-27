def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = list([costs[0][0]]) # 연결을 확인하는 집합
    visit = [0] * n
    # Kruskal 알고리즘으로 최소 비용 구하기
    while sum(visit) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.append(cost[0])
                connect.append(cost[1])
                visit[cost[0]] = 1
                visit[cost[1]] = 1
                answer += cost[2]
                break
                
    return answer