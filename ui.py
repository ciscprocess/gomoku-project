#-------------------------------------------------------------------------------
# Name:        ui
# Purpose:     Provides user interface routines and drives the whole program
#
# Author:      Nathan
#
# Created:     14/10/2012
# Copyright:   (c) Nathan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import gomoku
import graphics
import ai
def mainloop():
    var = raw_input("--> ")
    while parseinput(var):
        var = raw_input("--> ")

def parseinput(input):
    if input[:5] == 'move[':
        #x = int(input[5])
        #y = input[6]
        x = None
        y = None

        if int(input[6], 30) < 10:
            x = int(input[5:7]) - 1
            y = int(input[7], 30) - 10
        else:
            x = int(input[5]) - 1
            y = int(input[6], 30) - 10

        gomoku.state = gomoku.state.play((x, y), 'p')
        graphics.clear()
        graphics.drawBoard(gomoku.state)
        #print 'Score: ', gomoku.state.score()
        agent = ai.MinimaxAgent()
        act = agent.getAction(gomoku.state)
        gomoku.state = gomoku.state.play(act, 'c')

        if gomoku.state == None:
            print 'Oh shizzatch!'
            return

        graphics.clear()
        graphics.drawBoard(gomoku.state)
        print 'Tree nodes expanded: ' + str(agent.expanded)
        return True
    elif input[:4] == 'quit':
        return False
    else:
        print 'Unrecognized command'
        return True
