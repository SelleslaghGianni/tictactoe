# We are going to build a one-player tic-tac-toe game, which we can play in the command-line. 
# Initially, we’ll make an empty game board and then we’ll take inputs from the player 
# and we’ll check for the winning condition and if the whole board gets filled and no one wins, 
# we’ll declare the result as “Tie” and ask users if they want to restart the game.

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def emptyBoard(): # Creating an empty board if the player wants to start playing or replay.
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def printBoard(): # Printing the board
    print("_______")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("_______")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("_______")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("_______")

def takeInput(): # Taking the input
    print("Please enter your answer. Use the commands as instructed, such as 'mid-L', 'bot-R' and 'top-M'.")

    playerInput = input()

    if playerInput == "top-L":
        useInput(board[0])
    elif playerInput == "top-M":
        useInput(board[1])
    elif playerInput == "top-R":
        useInput(board[2])
    elif playerInput == "mid-L":
        useInput(board[3])
    elif playerInput == "mid-M":
        useInput(board[4])
    elif playerInput == "mid-R":
        useInput(board[5])
    elif playerInput == "bot-L":
        useInput(board[6])
    elif playerInput == "bot-M":
        useInput(board[7])
    elif playerInput == "bot-R":
        useInput(board[8])
    else:
        takeInput()

def useInput(position): 
    # Checking if the input is valid and then putting the input of the player on the board.
    if position == ('X' or 'Y'):
        print("This position is already used. Please try another position.")
        takeInput()
    else:
        if playerX == True:
            position = 'X'
        else:
            position = 'O'

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
    if (board.count('X') + board.count('Y')) == 9:
        return True
    else:
        return False

def gameWon():
    print("You have won! Congratulations! You have won exactly nothing but fame!")
    print("Do you want to play again? Enter 'Yes' or 'No'.")
    playAgain = input()
    if playAgain == "Yes":
        emptyBoard()
    else:
        print("Thank you for playing!")
        exit()


while fullBoardCheck() == False:
    print("Welcome to the game of Tic Tac Toe. This game is played via the Command Line Interface as you know.")
    print("Time to play! Player X gets to start first.")
    printBoard()
    playerX = True
    takeInput()
    if winCheck():
        gameWon()
        continue
    printBoard()
    playerX = False
    takeInput()
    if winCheck():
        gameWon()
        continue