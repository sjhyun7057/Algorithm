def solution(board, skill):
    cnt = 0
    empty_board = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for sk in skill:
        x, r1, c1, r2, c2, degree = sk
        empty_board[r1][c1] += degree*((-1)**x)
        empty_board[r1][c2+1] += degree*((-1)**(x+1))
        empty_board[r2+1][c1] += degree*((-1)**(x+1))
        empty_board[r2+1][c2+1] += degree*((-1)**x)

    for i in range(len(board)):
        for j in range(1,len(board[0])):
            empty_board[i][j] += empty_board[i][j-1]
    
    for i in range(1,len(board)):
        for j in range(len(board[0])):
            empty_board[i][j] += empty_board[i-1][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += empty_board[i][j]
            if board[i][j] > 0:
                cnt += 1       
    return cnt