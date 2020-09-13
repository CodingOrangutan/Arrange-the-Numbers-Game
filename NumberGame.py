from random import shuffle
import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=400, height = 450, caption="GameWindow")

#Defining Variables
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
images = []
board = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]]
clickcol = 0
clickrow = 0
endboard = [[13, 14, 15, 0], 
            [9, 10, 11, 12], 
            [5, 6, 7, 8,], 
            [1, 2, 3, 4]]
turn = 0

Banner=pyglet.image.load ('Banner.jpg')

def CreateBoard (board):
    global images
    shuffle (numberlist)
    count = 0
    for i in range (4):
        for j in range (4):
            board[i][j] = numberlist[count]
            images.append(pyglet.image.load(str(count)+'.jpg'))
            count+=1

def handleMove(x,y):
    global clickcol
    global clickrow
    clickcol = x//100
    clickrow = y//100
    CheckforEmpty (clickcol, clickrow)

def DisplayImages ():
    for i in range(4):
        #Draw each row
        y = 100*i
        for j in range(4):
            #draw each piece, first getting position
            x = 100*j
            images[board[i][j]].blit(x,y)


def CheckforEmpty (clickcol, clickrow):
    global board
    if (clickcol < 3 and board[clickrow][clickcol+1] == 0):
        SwapPieces(clickrow,clickcol, clickrow, clickcol+1)
    elif (clickcol > 0 and board[clickrow][clickcol-1] == 0):
        SwapPieces(clickrow,clickcol, clickrow, clickcol-1)
    elif (clickrow < 3 and board[clickrow+1][clickcol] == 0):
        SwapPieces(clickrow,clickcol, clickrow+1, clickcol)
    elif (clickrow > 0 and board[clickrow-1][clickcol] == 0):
        SwapPieces(clickrow,clickcol, clickrow-1, clickcol)
    else:
        music = pyglet.resource.media('Bark.mp3')
        music.play()

def SwapPieces (clickrow, clickcol, targetrow, targetcol): 
    global board
    global turn
    board[targetrow][targetcol] = board[clickrow][clickcol]
    board[clickrow][clickcol] = 0
    turn += 1
    
def EndGame ():
    global board
    if endboard == board:
        label = pyglet.text.Label ('Congratulations! You won in '+str(turn)+' turns!'+' Press R to restart.', 
                                    font_name= "Times", 
                                    font_size= 12, 
                                    x= 10, y= 420)
        label.draw ()
    else:
        turnlabel =  pyglet.text.Label ('Turn: '+str(turn), 
                                    font_name= "Times", 
                                    font_size= 18, 
                                    x= 10, y= 420)
        turnlabel.draw ()
    
def FinishGame ():
    global board
    board=[[13, 14, 0, 15], 
            [9, 10, 11, 12], 
            [5, 6, 7, 8,], 
            [1, 2, 3, 4]]
    
@window.event
def on_draw():
    window.clear()
    DisplayImages ()
    EndGame()

@window.event
def on_mouse_press (x, y, button, modifiers):
    handleMove(x,y)

@window.event 
def on_key_press(symbol, modifiers):
    global turn
    if (symbol == key.Q):
        FinishGame ()
    if (symbol == key.R):
        CreateBoard(board)
        turn = 0

CreateBoard(board)  
pyglet.app.run()
