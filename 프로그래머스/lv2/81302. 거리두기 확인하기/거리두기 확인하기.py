def solution(places):
    def make_arr(places):
        place_arr = []
        for place in places:
            arr = []
            for p in place:
                arr.append(list(p))
            place_arr.append(arr)
        return place_arr
    place_arr = make_arr(places)
    dist_dict = {'P': 0, 'O': 1, 'X': 2}
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    
    def dfs(i,j, min_dist):
        nonlocal check
        
        if min_dist <= 0 :
            return
        
        # if 0< min_dist <= 2 and place[i][j] == 'P':
        #     check = 1
        #     return
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<5 and 0<=nj<5 and not visit[ni][nj]:
                if 0< min_dist <= 2 and place[ni][nj] == 'P':
                    check = 1
                    return
                visit[ni][nj] = 1
                dfs(ni, nj, min_dist-dist_dict[place[ni][nj]])
                visit[ni][nj] = 0
                
    answer = []            
    for place in place_arr:
        check = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visit = [[0]*5 for _ in range(5)]
                    visit[i][j] = 1
                    dfs(i, j, 2)
                    if check:
                        break
            if check:
                answer.append(0)
                break
        if not check:
            answer.append(1)
    return answer