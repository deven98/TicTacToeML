from Board import Board

gameOne = Board()

gameOne.makeMove(1)
gameOne.makeMove(1)
gameOne.makeMove(1)
gameOne.makeMove(1)
gameOne.makeMove(0)

gameOne.displayBoard()
print(gameOne.isWin())