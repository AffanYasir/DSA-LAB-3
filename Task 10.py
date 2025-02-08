def check_winner(board):
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
       
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
       
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    
    return None

board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
winner = check_winner(board)
if winner:
    print(f"Winner: {winner}" if winner != "Draw" else "It's a draw!")