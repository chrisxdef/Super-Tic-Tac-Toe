import Tkinter as tk
import sys
sys.path.append('../model')
sys.path.append('../controller')
from tictactoe import *
from ai import *

class App(tk.Frame):

    def __init__(self, master=None):
        self.s = 700 / 3  # side length of each square panel on our board
        self.symbols = {0: "", 1: "O", 2: "X"}
        self.buttonList = []  # list of references to all panel buttons on our board
        self.recentClick = 0
        top = tk.Frame.__init__(self, master)
        self.grid()

        for r in range(0, 3):
            for c in range (0, 3):
                f = tk.Frame(top, height = self.s, width = self.s, highlightbackground="black", highlightcolor="black", highlightthickness="5")
                f.grid(row=r, column=c)
                b = tk.Button(f, height=10, width=25, text="X", relief="flat", bd=0)
                b.position = (3*r+c)
                b.config(command=lambda widget=b: self.outputNumber(widget))
                b.grid(row=r, column=c)
                self.buttonList.append(b)

    def outputNumber(self, button):
        self.recentClick = button.position

    def update(self, board):
        for i in range (0, 8):
            symb = self.symbols[board[i]]
            print symb
            #self.buttonList[i].config(text=self.symbols[board[i]])


app = App()
app.master.title("Tic Tac Toe")
app.mainloop()
if __name__ == "__main__":
    gameBoard = [0,0,0,0,0,0,0,0,0]
    over = False
    humanTurn = True
    while not over:
        newInfo = (game(gameBoard, app.recentClick, humanTurn))
        gameBoard = newInfo[0]
        app.update(gameBoard)
        humanTurn = not newInfo[1]
        over = newInfo[2]