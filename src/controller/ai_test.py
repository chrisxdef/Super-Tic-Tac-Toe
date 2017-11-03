import sys
from ai import Node, SuperNode

def printChildren(node, max_depth, depth=0):
	s = ""
	for i in range(depth):
		s += "\t"
	print s + str(node.gameBoard)
	depth+=1
	if depth < max_depth:
		for child in node.children:
			printChildren(child,max_depth,depth)	


subBoard = [0,0,0,0,0,0,0,0,0]         
gameBoard = []
for i in range(9):
	gameBoard.append(subBoard[:])


n = SuperNode(1,gameBoard)
n.createTree(3)
print 'Done createTree()'

printChildren(n, 6)
