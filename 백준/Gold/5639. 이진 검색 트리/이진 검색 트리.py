'''
1. 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
2. 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
3. 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.
50    5
30    28
24    24
5     45
28    30
45    60
98    52
52    98
60    50
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


arr = []
# 정확한 노드의 개수가 안나왔기 때문에 try, except 예외 처리
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
    

def tree(lst):
    if len(lst) == 0: # 받은 트리가 0이면 리턴
        return
    
    small_lst, large_lst = [], []
    #첫번째 값 중간
    mid = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] > mid:
            small_lst = lst[1:i]
            large_lst = lst[i:]
            break
    else:
        #모두 작은 경우
        small_lst = lst[1:]
    
    #왼, 오 순으로 후위 순위 후 출력
    tree(small_lst)
    tree(large_lst)
    print(mid)
    
tree(arr)