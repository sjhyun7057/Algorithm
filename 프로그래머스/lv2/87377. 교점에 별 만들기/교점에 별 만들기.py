def solution(line):
    # 교점찾기
    lst = []
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            a,b,e = line[i]; c,d,f = line[j]
            if a*d - b*c !=0 : # 근의 공식
                x = (b*f-e*d)/(a*d-b*c) ; y = (e*c-a*f)/(a*d-b*c)
                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    if (x,y) not in lst:
                        lst.append((x,y))
    min_x, max_x, min_y, max_y = min(lst)[0],max(lst)[0], min(lst, key=lambda x : x[1])[1], max(lst, key=lambda x : x[1])[1]
    answer = [['.']*(max_x - min_x+1) for _ in range(max_y-min_y+1)]
    for i in lst:
        x, y = i
        a, b = abs(max_y-y) , abs(min_x-x)
        answer[a][b] = '*'
    for i,j in enumerate(answer):

        answer[i] = ''.join(j)
    return answer
