import Tkinter as tk
import sys
sys.path.append('../model')
sys.path.append('../controller')
from tictactoe import *
from ai import *

root = tk.Tk()
root.title("Tic-Tac-Toe")
O = tk.PhotoImage(file = "O.gif")
X = tk.PhotoImage(file="X.gif")
blank = tk.PhotoImage(file="blank.gif")
symbols = {0:blank, 1:O, 2:X}
labelList = []
state = GameState(gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0])

def endGame(overBoard):
    c = 0
    for val in overBoard:
        labelList[c].configure(image=symbols.get(val))
        labelList[c].unbind('<Button-1>')
        c += 1
    messageBox.configure(text=state.getPrompt())

def takeTurn(event):
    state.updateHuman(event.widget.name)
    messageBox.configure(text=state.getPrompt())
    if state.getGameOver():
        endGame(state.getBoard())
    else:
        state.updateAI()
        messageBox.configure(text=state.getPrompt())
        board = state.getBoard()
        if state.getGameOver():
            endGame(board)
        counter = 0
        for value in board:
            labelList[counter].configure(image = symbols.get(value))
            if value != 0:
                labelList[counter].unbind('<Button-1>')  #inefficient
            counter+=1
i = 0
for r in range(0, 3):
    for c in range (0, 3):
        label = tk.Label(root, borderwidth=2, relief="solid", image=blank)
        label.image = blank
        label.grid(row=r, column=c)
        label.bind('<Button-1>', takeTurn)
        label.name = i
        i+=1
        labelList.append(label)

messageBox = tk.Label(root, relief="groove", width=58, borderwidth=5, bg="green", font="Times 12 bold", text=state.getPrompt())
messageBox.grid(row=4, columnspan=9, sticky="nsew")

root.mainloop()



