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
    graphics.clear()
    graphics.drawBoard(state)
    ui.mainloop()
    for i in xrange(10):
        for ii in xrange(10):
            state.play((i, ii), 'p')
            graphics.clear()
            graphics.drawBoard(state)

if __name__ == '__main__':
    main()
