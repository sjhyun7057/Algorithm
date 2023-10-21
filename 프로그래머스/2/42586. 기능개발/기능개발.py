def solution(progresses, speeds):
    from collections import deque
    q = deque(progresses)
    speed_q = deque(speeds)
    answer = []
    cnt = 0
    while q:
        for i in range(len(q)):
            q[i] += speed_q[i]
        while q[0] >= 100:
            cnt += 1
            q.popleft()
            speed_q.popleft()
            if not q:
                break
        if cnt:
            answer.append(cnt)
            cnt = 0
    return answer