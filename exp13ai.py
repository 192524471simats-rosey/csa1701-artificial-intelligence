def minimax(board, isMax):
    if "O" in board and check_win(board, "O"):
        return 1
    if "X" in board and check_win(board, "X"):
        return -1
    if " " not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if isMax else "X"
            scores.append(minimax(board, not isMax))
            board[i] = " "

    return max(scores) if isMax else min(scores)

def check_win(b, p):
    return any(all(b[i] == p for i in line) for line in
               [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)])

board = [" "] * 9
print("Best score:", minimax(board, True))
