import sys
sys.path.append("../controller")
from ai import Node

winBoards = [Set([0,1,2]),Set([3,4,5]),Set([6,7,8]),Set([0,3,6]),Set([1,4,7]),Set([2,5,8]),Set([0,4,8]),Set([2,4,6])]

def fullBoard(board):
        for i in board:
                if i == 0:
                        return False
        return True

def winBoard(board):
        player1 = []
        player2 = []
        for i in range(len(board)):
                if board[i] == 1:
                        player1.append(i)
                elif board[i] == 2:
                        player2.append(i)
        player1 = Set(player1)
        player2 = Set(player2)
        for s in winBoards:
                if s.issubset(player1):
                        return 1
                elif s.issubset(player2):
                        return 2
        return False

def game(gameBoard, human, ai):
	running = True
	turn = 1
	while(running):
		print gameBoard
		if turn == human:
			index = int(raw_input("Show me your moves!\t"))
			while(gameBoard[index] != 0):
				index = int(raw_input("Show me your moves!\t"))
			gameBoard[index] = human
			turn = ai
		else:
			print "Robot's Turn\n"
			node = Node(ai, gameBoard)
			node.createTree(3)
			gameBoard = node.minimax(False, ai, True)
			turn = human
		if winBoard(gameBoard) == human:
			print "GG! You Win!"
			running = False
		elif winBoard(gameBoard) == ai:
			print "GG! Robot Wins!"
			running = False
		elif fullBoard(gameBoard):
			print "GG! It's a draw!"
			running = False		


if __name__ == "__main__":
	gameBoard = [0,0,0,0,0,0,0,0,0]
	human = 1
	ai = 2
	game(gameBoard, human, ai)	
