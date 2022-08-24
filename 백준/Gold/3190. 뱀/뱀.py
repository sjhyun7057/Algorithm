from collections import deque
# 뱀의 초기 위치 0,0 X초 후 L은 왼쪽으로 90도 D는 오른쪽으로 90도 회전
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

apple = [list(map(int,input().split())) for _ in range(K)]

L = int(input()) # 움직임 횟수
move_dict = {}
for _ in range(L):
    key, value = input().split()
    move_dict[int(key)] = value
# L이면 k에 -1 D면 k에 + 1 # 4로나눠서 나머지로 계산
dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

location = deque([[1,1]])


time = 0

def dummy_game():
    global time
    k = 0
    while True:
        if time in move_dict.keys():
            if move_dict[time] == 'D':
                k += 1
            elif move_dict[time] == 'L':
                k -= 1
                if k < 0:
                    k = 4 + k
            k %= 4

        i, j = location[-1] # 머리 늘리기
        i += di[k]; j += dj[k]
        time += 1

        if i > N or i < 1 or j < 1 or j > N or [i, j] in location:
            break
        if [i,j] not in apple: # 길이는 그대로 늘어난 머리는 그대로 유지
            location.append([i,j])
            location.popleft() # 꼬리 줄이기
        else: # 사과 먹기
            location.append([i,j])
            apple.remove([i, j])

dummy_game()

print(time)