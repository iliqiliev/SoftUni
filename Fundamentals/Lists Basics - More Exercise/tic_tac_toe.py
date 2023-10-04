board = [input().split() for line in range(3)]
winner = 0

for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] and board[0][i]: # columns
        winner = board[0][i]
    elif board[i][0] == board[i][1] == board[i][2] and board[i][0]: # rows
        winner = board[i][0]

if board[1][1]: # diagonals
    if board[0][0] == board [1][1] == board[2][2]: 
        winner = board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[1][1]
        
if winner == "0":
    print("Draw!")
elif winner == "1":
    print("First player won")
else:
    print("Second player won")