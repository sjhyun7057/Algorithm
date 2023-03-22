import sys
input = sys.stdin.readline
N = int(input())

lst = [int(input()) for _ in range(N)]


lst.sort()

for _ in range(N):
    print(lst[_])
