import sys
from ai import Node

gameBoard = [0,0,0,0,0,0,0,0,0]         
n = Node(1,gameBoard)
n.createTree()
print 'Done createTree()'

result = n.minimax(True)

print result
