from Board import Board
from Computer import Computer

mainBoard = Board()
mainComputer = Computer(mainBoard)

mainComputer.playGames(10)

print(mainComputer.winList)
print(mainComputer.lossList)
