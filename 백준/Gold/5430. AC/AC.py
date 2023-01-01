import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def AC(fct):
    global cnt
    if fct == 'R':
        cnt += 1
    elif fct == 'D':
        if lst:
            if cnt%2:
                lst.pop()
            else:
                lst.popleft()
        else:
            return False
    return True

for ts in range(T):
    fct = deque(input().strip())
    length = int(input())
    if length:
        lst = deque(input().strip()[1:-1].split(','))
    else:
        lst = input()
        lst = deque()
    break_point = 1
    cnt = 0
    while fct:
        f = fct.popleft()
        if not AC(f):
            print('error')
            break_point = 0
            break
    if break_point:
        if cnt%2:
            lst.reverse()
        print('[' + ','.join(lst) + ']')