from collections import deque
N, M = map(int, input().split())

n_q = deque(map(int, input().split()))
answer = 0
q = deque()
while n_q:
    q.append(n_q.popleft())
    if sum(q) == M:
        answer += 1
    elif sum(q) > M:
        while sum(q) > M:
            q.popleft()
            if sum(q) == M:
                answer += 1
                break
    
print(answer)