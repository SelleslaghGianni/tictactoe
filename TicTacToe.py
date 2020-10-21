# Tic Tac Toe game. Currently no AI. Still have to look into it.

def printBoard(): # Printing the board
    print("-------")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-------")

def takeInput(): # Taking the input
    print("Please enter your answer. Use the commands as instructed, such as 'mid-L', 'bot-R' and 'top-M'.")

    playerInput = input()

    if playerInput == "top-L":
        board[0] = player
    elif playerInput == "top-M":
        board[1] = player
    elif playerInput == "top-R":
        board[2] = player
    elif playerInput == "mid-L":
        board[3] = player
    elif playerInput == "mid-M":
        board[4] = player
    elif playerInput == "mid-R":
        board[5] = player
    elif playerInput == "bot-L":
        board[6] = player
    elif playerInput == "bot-M":
        board[7] = player
    elif playerInput == "bot-R":
        board[8] = player
    else:
        takeInput()


def winCheck(): # Checking if a player has won.
    if board[0] == board[1] == board[2] == ('X' or 'O'): # Top line horizontal
        return True
    elif board[3] == board[4] == board[5] == ('X' or 'O'): # Middle line horizontal
        return True
    elif board[6] == board[7] == board[8] == ('X' or 'O'): # Bottom line horizontal
        return True
    elif board[0] == board[3] == board[6] == ('X' or 'O'): # Left line vertical
        return True
    elif board[1] == board[4] == board[7] == ('X' or 'O'): # Middle line vertical
        return True
    elif board[2] == board[5] == board[8] == ('X' or 'O'): # Right line vertical
        return True
    elif board[0] == board[4] == board[8] == ('X' or 'O'): # From top-left to bot-right
        return True
    elif board[2] == board[4] == board[6] == ('X' or 'O'): # from top-right to bot-left
        return True 
    else:
        return False

def fullBoardCheck(): # Check if the board is full, if True then the game will be declared a Tie.
    counter = 0
    Ycounter = 0
    for i in board:
        if i == 'X':
            counter = counter + 1
        elif i == 'O':
            Ycounter = Ycounter + 1
    if counter + Ycounter == 9:
        return True
    else:
        return False

def gameFinished(): # If the game is over, does the user want to play again?
    printBoard()
    print("The game has ended!")
    print("Do you want to play again? Enter 'Yes' or 'No'.")
    playAgain = input()
    if playAgain == "Yes":
        return True
    else:
        print("Thank you for playing!")
        return False

# Declaring some variables.
gameState = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# Printing the start of the game.
print("Welcome to the game of Tic Tac Toe. This game is played via the Command Line Interface as you know.")
print("Enjoy the game!")
# Game starts here. The while loop is basically 2x the same thing.
while gameState:
    print("Processing....")
    printBoard()
    player = 'X'
    takeInput()
    if winCheck():
        print("You won!! Let all your friends know!")
        if gameFinished():
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            continue
        else:
            gameState = False
            continue
    if fullBoardCheck(): 
        print("You have tied the game. Please let all your friends know you both SUCK! :D")
        if gameFinished():
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            continue
        else:
            gameState = False
            continue
    printBoard()
    player = 'O'
    takeInput()
    if winCheck():
        print("You won!! Let all your friends know!")
        if gameFinished():
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            continue
        else:
            gameState = False
            continue
    elif fullBoardCheck(): 
        print("You have tied the game. Please let all your friends know you both SUCK! :D")
        if gameFinished():
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            continue
        else:
            gameState = False
            continue
    