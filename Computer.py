# Class that runs all games and stores them into a file/list
from random import randint

class Computer(object):

    def __init__(self,board):
        self.winList = []
        self.lossList = []
        self.board = board

    def playGames(self, numberOfGames):

        for game in range(numberOfGames):
            self.playSingleGame()


    def playSingleGame(self):

        while self.board.isWin() is 0:
            self.board.makeMove(randint(0,8))

        if self.board.isWin is 1:
            self.winList.append(self.board.moveList)

        print(self.board.moveList)

        self.board.resetBoard()
