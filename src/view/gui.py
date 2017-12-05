mport Tkinter as tk
import sys
sys.path.append('../model')
sys.path.append('../controller')
from tictactoe import GameState
from ai import *
class App(tk.Frame):
        symbols = {0 : "", 1 : "O", 2 : "X"}

    def __init__(self, master=None):
        self.s = 700 / 3  # side length of each square panel on our board
        self.buttonList = []  # list of references to the tiles of our super board
        top = tk.Frame.__init__(self, master)
        self.grid()
	self.GameState()

        for r in range(0, 8):
            for c in range (0, 8):
                f = tk.Frame(top, height = self.s, width = self.s, highlightbackground="black", highlightcolor="black", highlightthickness="5")
                f.grid(row=r, column=c)
                b = tk.Button(f, height=10, width=25, text="X", relief="flat", bd=0)
                b.grid(row=r, column=c)
                self.buttonList.append(b)

    def update(self):
	currentBoard = GameState.gameBoard
        for i in range(0, 8):
		for j in range(0, 8):
	            buttonList[i * 9 + j].config(text = symbols[currentBoard[i][j]])

#Todo: buttonpush = raw input, or editing gameBoard directly? reading gameBoard, disabling buttons not in play

app = App()
app.master.title("Tic Tac Toe")
app.mainloop()

#main loop
#game([0,0,0,0,0,0,0,0,0], 1, 2)
