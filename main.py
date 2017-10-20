from Board import Board
from Computer import Computer

mainBoard = Board()
mainComputer = Computer(mainBoard)

# Computer saves data for n random games
mainComputer.playGames(100000)

# Start Human-Computer game here

while ((mainBoard.isWin() is not 1)):

    print("Move " + str(mainBoard.movesPlayed))

    mainComputer.makeMove(mainBoard.movesPlayed,mainBoard)

    mainBoard.displayBoard()

    if(mainBoard.isWin()):
        print("Computer won!")
        break

    move = input("Enter square to move on: ")

    mainBoard.makeMove(int(move))

    mainBoard.displayBoard()

    print("Win value : " + str(mainBoard.isWin()))