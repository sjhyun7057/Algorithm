N = int(input())

chae = 100
bbeum = 0

minus_lst = list(map(int,input().split()))
plus_lst = list(map(int,input().split()))

max_bbeum = 0

def recur(i, c, b):
    global max_bbeum
    if c <= 0:
        return
    if i == N:
        if max_bbeum < b:
            max_bbeum =b
        return
    recur(i+1, c-minus_lst[i], b + plus_lst[i])
    recur(i+1, c, b)
    
recur(0, 100, 0)

print(max_bbeum)