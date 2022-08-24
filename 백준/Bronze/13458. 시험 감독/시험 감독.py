N = int(input()) # 시험장 수
A_lst = list(map(int, input().split())) # 각각의 시험장에 들어가는 사람 수
B, C = map(int, input().split()) # 총시험감독관의 감시자수, 부감독관의 감시자수

cnt = 0
for i in range(N):
    cnt += 1
    A = A_lst[i]
    A -= B
    if A <= 0:
        continue
    if A%C:
        cnt += (A//C) + 1
    else:
        cnt += A//C
print(cnt)