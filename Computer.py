# Class that runs all games and stores them into a file/list
from random import randint

class Computer(object):

    # Contains a win list to store all games won, similarly a loss list
    def __init__(self,board):
        self.winList = []
        self.lossList = []
        self.board = board

    # Play games a specific number of times
    def playGames(self, numberOfGames):

        for game in range(numberOfGames):
            self.playSingleGame()

    # Plays a single game with the board provided and resets values after play
    def playSingleGame(self):

        while self.board.isWin() is 0:
            self.board.makeMove(randint(0,8))

        # Only triggers if player 1 wins
        if self.board.isWin() is 1:
            if self.board.playerToMove is 2:
                self.winList.append(self.board.moveList)

        print(self.board.moveList)

        self.board.resetBoard()
