#-------------------------------------------------------------------------------
# Name:        Gomoku AI Project
# Purpose:
#
# Author:      Nathan Korzekwa
#
# Created:     14/10/2012
# Copyright:   (c) Nathan Korzekwa 2012
# Licence:     MIT License
#-------------------------------------------------------------------------------
import graphics
import game
import ui
import ai


state = game.GameState()
def main():
    #graphics.clear()
    #graphics.drawBoard(state)
    #ui.mainloop()
    money = 10
    count = 0
    for fives in xrange(3):
        for fours in xrange(3):
            for threes in xrange(4):
                for twos in xrange(6):
                    for ones in xrange(11):
                        if (fives * 6 + fours * 4 + threes * 3 + twos * 2 + ones) == money:
                            count += 1

    print str(count)
##    for i in xrange(10):
##        for ii in xrange(10):
##            state.play((i, ii), 'p')
##            graphics.clear()
##            graphics.drawBoard(state)

if __name__ == '__main__':
    main()
