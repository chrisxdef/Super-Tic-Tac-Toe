import sys
from ai import Node, minimax

gameBoard = [0,0,0,0,0,0,0,0,0]         
n = Node(1,gameBoard)
n.createTree()
print 'Done createTree()'

for child in n.children:
	print child.gameBoard
	for child2 in child.children:
		print "		" + str(child2.gameBoard)
		for child3 in child2.children:
			print "			" + str(child3.gameBoard)

