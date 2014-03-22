#-------------------------------------------------------------------------------
# Name:        ai
# Purpose:     makes the game smart
#
# Author:      Nathan
#
# Created:     15/10/2012
# Copyright:   (c) Nathan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import game
from Queue import PriorityQueue
from math import log, exp

def invsig(sigma):
    sigma = float(sigma)
    x = log(1 - sigma) - log(sigma)
    return x

def sigmoid(x):
    x = float(x)
    return 1/(1 + exp(-x))

def dsigmoid(x):
    return sigmoid(x)*(1 - sigmoid(x))

def test(state):
    var = []
    for i in range(0, 709009):
        var.append(i % 555 + 99 * 77)
        state.score()
def linearate(bounds, n):
    length = bounds[0] - bounds[1]
    period = length / float(n)
    points = []
    for i in xrange(n):
        points.append((i + 1) * period)
    return points

def sigmoiderate(bounds, n):
    return [sigmoid(x) for x in linearate(bounds, n)]

class MinimaxAgent():
    def __init__(self):
        self.depth = 100
        self.expanded = 0
        self.pint = 1
        self.bounds = [invsig(0.01), -invsig(0.01)]

    def getAction(self, state):
        var = self.minimax(state, 0, 0, 999999)
        return var[1][0]

    def minimax(self, state, curDepth, curIndex, alphabeta):
        self.expanded += 1

        if curIndex == 2:
            curIndex = 0

        actions = state.legalMoves

        if curDepth / 2 == self.depth: #Terminal State From Depth Limit
            return (state.score(), [None])

        if curIndex == 0:
            maxVal = (-999999, [None])
            for a in actions:
                t = self.minimax(state.play(a, 'c'), curDepth + 1, curIndex + 1, maxVal[0])
                if t[0] > maxVal[0]:
                    maxVal = (t[0], [a])

            sco = state.score()
            if (len(actions) == 0) | (sco != 0): #REAL Terminal state
                return (sco, [None])

            return maxVal
        else:
            minVal = (999999, [None])
            l = PriorityQueue()

            for a in actions:
                t = self.minimax(state.play(a, 'p'), curDepth + 1, curIndex + 1, minVal[0])
                l.put(t)

            weights = sigmoiderate(self.bounds, len(actions))
            weighted_value = 0

            while not l.empty():
                w = weights.pop()
                a = l.get()
                weighted_value += w * a[0]

            minVal = (weighted_value, minVal[1])

            sco = state.score()
            if (len(actions) == 0) | (sco != 0): #REAL Terminal state
                #print 'Terminal state! Hash: ' + str(state.hash)
                return (sco, [None])

            return minVal