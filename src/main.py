from graphics import Window
from cell import Cell


win = Window(800, 600)


c = Cell(win)
c.has_left_wall = False
c.draw(50, 50, 100, 100)

c = Cell(win)
c.has_right_wall = False
c.draw(125, 125, 200, 200)

c = Cell(win)
c.has_bottom_wall = False
c.draw(225, 225, 250, 250)

c2 = Cell(win)
c2.has_top_wall = False
c2.draw(300, 300, 500, 500)

c.draw_move(c2)

win.wait_for_close()
