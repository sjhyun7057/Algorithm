def solution(info, edges):
    visit = [0]*len(info)
    visit[0] = 1
    answer = 0
    def dfs(sheep, wolf, edges):
        nonlocal answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return
        
        for edge in edges:
            p_node, c_node = edge            
            if visit[p_node] and not visit[c_node]:
                visit[p_node] = 1
                visit[c_node] = 1
                if info[c_node] == 0:
                    dfs(sheep+1, wolf, edges)
                    visit[c_node] = 0
                else:
                    dfs(sheep, wolf+1, edges)
                    visit[c_node] = 0
                
    dfs(1, 0, edges)

    return answer
