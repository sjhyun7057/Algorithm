'''
문자열의 뒤에 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다.
'''
from collections import deque

S = deque(input().strip())
T = deque(input().strip())

while len(T)>len(S):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.reverse()
        T.popleft()
    if len(T) == len(S):
        if T == S:
            print(1)
        else:
            print(0)
        