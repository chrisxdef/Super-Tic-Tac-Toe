import Tkinter as tk
import sys
sys.path.append('../model')
sys.path.append('../controller')
from tictactoe import game
from ai import *
class App(tk.Frame):

    def __init__(self, master=None):
        self.s = 700 / 3  # side length of each square panel on our board
        self.buttonList = []  # list of references to the tiles of our super board
        self.symbols = {0 : "", 1 : "O", 2 : "X"}
        top = tk.Frame.__init__(self, master)
        self.grid()

        for r in range(0, 3):
            for c in range (0, 3):
                f = tk.Frame(top, height = self.s, width = self.s, highlightbackground="black", highlightcolor="black", highlightthickness="5")
                f.grid(row=r, column=c)
                b = tk.Button(f, height=10, width=25, text="X", relief="flat", bd=0)
                b.grid(row=r, column=c)
                self.buttonList.append(b)

    def update(self):
        for i in range(0, 8):
            #buttonList[i].config(text = symbols[currentBoard[i]])
            pass


#Todo: buttonpush = raw input, or editing gameBoard directly? reading gameBoard, disabling buttons not in play

app = App()
app.master.title("Tic Tac Toe")
app.mainloop()

#main loop
#game([0,0,0,0,0,0,0,0,0], 1, 2)