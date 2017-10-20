from Board import Board
from Computer import Computer

mainBoard = Board()
mainComputer = Computer(mainBoard)

# Computer saves data for n random games
mainComputer.playGames(500000)

# Creates a list of first moves
commonList = []
for game in mainComputer.winList:
    commonList.append(game[0])

# Prints recommended first move
print(mainComputer.most_common(commonList))

secondMoveList = []

for game in mainComputer.winList:
    if game[0] is 4 and game[1] is 3:
        secondMoveList.append(game)

commonList.clear()

for game in secondMoveList:
    commonList.append(game[2])

print(mainComputer.most_common(commonList))

thirdMoveList = []

for game in mainComputer.winList:
    if game[0] is 4 and game[1] is 3 and game[2] is 8 and game[3] is 6:
        thirdMoveList.append(game)

commonList.clear()

for game in thirdMoveList:
    commonList.append(game[4])

print(mainComputer.most_common(commonList))