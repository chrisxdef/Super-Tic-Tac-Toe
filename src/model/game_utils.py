from sets import Set
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
