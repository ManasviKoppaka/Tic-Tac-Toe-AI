board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ", 
         7:" ", 8:" ", 9:" "}

def showBoard():
    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])

def CheckWhoWins(player):
    if board[1] == board[2] and board[1]== board[3] and board[1] == player:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == player:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == player:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == player:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == player:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == player:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == player:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == player:
        return True
    else:
        return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def insert(player, position):
    if board[position] == " ":
        board[position] = player
        showBoard()
        if CheckWhoWins(player):
            showBoard()
            print(player, "is winner")
            quit()
        checkForDraw()
    else:
        print("Position is occupied. Try Again")
        position = int(input("Enter the new position: "))
        insert(player, position)

def play(player):
    if not checkForDraw():
        print(player, "turn")
        position = int(input("Enter the position (1-9): "))
        insert(player, position)
    else:
        print("Draw")
        quit()

def minimax(board, player):
    if CheckWhoWins("X"):
        return 1
    if CheckWhoWins("O"):
        return -1
    if checkForDraw():
        return 0
    if player == "computer":
        bestScore = -100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                score = minimax(board, "user")
                board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    
    if player == "user":
        bestScore = 100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                score = minimax(board, "computer")
                board[key] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore

def playComputer(player):
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = "X"
            score = minimax(board, "user")
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key
    insert(player, bestMove)



showBoard()

player1 = "X"
player2 = "O"

while True:
    playComputer(player1)
    if CheckWhoWins(player1):
        print("X wins the game!")
        break
    if checkForDraw():
        print("It's a Draw!")
        break


    play(player2)
    if CheckWhoWins(player2):
        print("O wins the game!")
        break
    if checkForDraw():
        print("It's a Draw!")
        break