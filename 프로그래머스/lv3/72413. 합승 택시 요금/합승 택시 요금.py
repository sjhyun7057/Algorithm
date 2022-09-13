def solution(n, s, a, b, fares):
    import heapq
    node_lst = [s, a, b]    
    dist_list = [[float('inf')]*(n+1) for _ in range(n+1)]
    tree_list = [[] for _ in range(n+1)]
    
    for fare in fares: 
        tree_list[fare[0]].append((fare[1],fare[2]))
        tree_list[fare[1]].append((fare[0],fare[2]))
    def make_table(start):
        dist_list[start][start] = 0
        heap = [[0,start]]
        while heap:
            dist, node = heapq.heappop(heap)
            for n, d in tree_list[node]: 
                distance = dist + d
                if dist_list[start][n] > distance:
                    dist_list[start][n] = distance
                    heapq.heappush(heap,[distance, n])

    for i in node_lst:
        make_table(i)
    min_dist = float('inf')
    
    for i in range(1, n+1):
        my_dist = dist_list[a][i] + dist_list[b][i] + dist_list[s][i]
        if min_dist > my_dist:
            min_dist = my_dist

    return min_dist