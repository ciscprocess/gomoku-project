#-------------------------------------------------------------------------------
# Name:        GameState
# Purpose:     Serves as the class that contains all necessary information for
#              the game at any given time
#
# Author:      Nathan
#
# Created:     14/10/2012
# Copyright:   (c) Nathan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import copy

side = 3
winlength = 3

class GameState():
    def __init__(self):
        self.grid = [['n' for x in xrange(side)] for x in xrange(side)] # Grid of gametiles
        self.legalMoves = [(x, y) for x in xrange(side) for y in xrange(side)]
        self.dynagrid = [[[0, 0, 0] for x in xrange(side)] for x in xrange(side)]
        self.hash = 0;

    def play(self, point, player):
        if self.legalMoves.count(point) == 0:
            print 'WARNING: An illegal move was attempted: ' + str(point)
            return None

        clone = copy.deepcopy(self)
        clone.grid[point[0]][point[1]] = player
        clone.legalMoves.remove(point)
        clone.hash = clone.hash + 10**(point[0] * 3 + point[1]) * {'p': 1, 'c': 2}[player]
        return clone

    def score(self):
        players = ['p', 'c']
        for player in players:
             # Form of: (row, col, diag)
            dynagrid = [[[0, 0, 0] for x in xrange(side)] for x in xrange(side)]
            thing = []
            col = 0
            row = 0

            for i in xrange(side):
                dynagrid[0][i] = [int(self.grid[0][i] == player)] * 3
                if self.grid[0][i] == player:
                    row += 1
                else:
                    row = 0
                if row > winlength - 1:
                    if player == 'p':
                        return -1
                    else:
                        return 1
            for i in xrange(side):
                dynagrid[i][0] = [int(self.grid[i][0] == player)] * 3
                if self.grid[i][0] == player:
                    col += 1
                else:
                    col = 0
                if col > winlength - 1:
                    if player == 'p':
                        return -1
                    else:
                        return 1

            for i in range(1, side):
                for ii in range(1, side):
                    if self.grid[i][ii] == player:
                        dynagrid[i][ii][2] = dynagrid[i - 1][ii - 1][2] + 1
                    else:
                        dynagrid[i][ii][2] = 0
                    if self.grid[i][ii] == player:
                        dynagrid[i][ii][1] = dynagrid[i - 1][ii][1] + 1
                    else:
                        dynagrid[i][ii][1] = 0
                    if self.grid[i][ii] == player:
                        dynagrid[i][ii][0] = dynagrid[i][ii - 1][0] + 1
                    else:
                        dynagrid[i][ii][0] = 0

                    if (dynagrid[i][ii][0] > winlength - 1) | (dynagrid[i][ii][1] > winlength - 1) | (dynagrid[i][ii][2] > winlength - 1):
                        if player == 'p':
                            return -2
                        else:
                            return 2

                    elif (dynagrid[i][ii][0] > winlength - 2) | (dynagrid[i][ii][1] > winlength - 2) | (dynagrid[i][ii][2] > winlength - 2):
                        if player == 'p':
                            return -1
                        else:
                            return 1

        return 0



