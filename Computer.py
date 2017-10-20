# Class that runs all games and stores them into a file/list
from random import randint
import itertools
import operator

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

        # Triggers if someone wins. "Win" here is player 1 winning and "Loss" implies a player 2 win.
        if self.board.isWin() is 1:
            if self.board.playerToMove is 2:
                self.winList.append(self.board.moveList[:])
            elif self.board.playerToMove is 1:
                self.lossList.append(self.board.moveList[:])

        self.board.resetBoard()

    def most_common(self,L):
        # get an iterable of (item, iterable) pairs
        SL = sorted((x, i) for i, x in enumerate(L))
        # print 'SL:', SL
        groups = itertools.groupby(SL, key=operator.itemgetter(0))

        # auxiliary function to get "quality" for an item
        def _auxfun(g):
            item, iterable = g
            count = 0
            min_index = len(L)
            for _, where in iterable:
                count += 1
                min_index = min(min_index, where)
            # print 'item %r, count %r, minind %r' % (item, count, min_index)
            return count, -min_index

        # pick the highest-count/earliest item
        return max(groups, key=_auxfun)[0]
