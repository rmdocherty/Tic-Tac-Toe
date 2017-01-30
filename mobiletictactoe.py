import os
board = [" "," "," "," "," "," "," "," "," "]
loop = 0
win = 0
def printBoard():
    print board[0],"|",board[1],"|",board[2]
    print board[3],"|",board[4],"|",board[5]
    print board[6],"|",board[7],"|",board[8]
def takeTurn():
    if loop%2 == 0:
        icon = "X"
    else:
        icon = "O"
    turn = int(raw_input("Which square do you wish to place your icon on? (1-9)"))
    if board[turn-1] == " ":
        board[turn-1] = icon
    else:
        print "That is not a valid move"
    os.system('clear')
    printBoard()
    checkWin(icon)
def checkWin(thing):
    global loop
    global win
    if (board[0] == thing) and (board[1] == thing) and (board[2] == thing):
        win = 1
    elif (board[3] == thing) and (board[4] == thing) and (board[5] == thing):
        win = 1
    elif (board[6] == thing) and (board[7] == thing) and (board[8] == thing):
        win = 1
    elif (board[0] == thing) and (board[3] == thing) and (board[6] == thing):
        win = 1
    elif (board[1] == thing) and (board[4] == thing) and (board[7] == thing):
        win = 1
    elif (board[2] == thing) and (board[5] == thing) and (board[8] == thing):
        win = 1
    elif (board[0] == thing) and (board[4] == thing) and (board[8] == thing):
        win = 1
    elif (board[2] == thing) and (board[4] == thing) and (board[6] == thing):
        win = 1
printBoard()
while win ==0:
    takeTurn()
    loop = loop + 1
os.system('clear')
print "You win!"
