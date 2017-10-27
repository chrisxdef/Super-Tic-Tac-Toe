import sys
from ai import Node

gameBoard = [0,0,0,0,0,0,0,0,0]         
n = Node(1,gameBoard)
n.createTree(3)
print 'Done createTree()'

for child in n.children:
	print child.gameBoard
	for child2 in child.children:
		print "\t"+str(child2.gameBoard)
		for child3 in child2.children:
			print "\t\t"+str(child3.gameBoard)
			for child4 in child3.children:
				print "\t\t\t"+str(child4.gameBoard)
				for child5 in child4.children:
					print "\t\t\t\t"+str(child5.gameBoard)
					for child6 in child5.children:
						print "\t\t\t\t\t"+str(child6.gameBoard)
				
		
	
