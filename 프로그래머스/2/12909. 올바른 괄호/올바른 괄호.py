def solution(s):
    from collections import deque
    lst = list(s)
    q = deque()
    
    for i in lst:
        if i == "(":
            q.append(i)
        else:
            if q:
                q.pop()
            else:
                return False
    if not q:
        return True
    else:
        return False