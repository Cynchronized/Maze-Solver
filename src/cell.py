from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0

        self._win = win
        self.visited = False

    # takes x/y cords of top-left corner and bottom-right corner of cell
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        # top-left
        self._x1 = x1
        self._y1 = y1

        # bottom-right
        self._x2 = x2
        self._y2 = y2

        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))

        # Black if wall is there, white if not
        left_color = "black"
        right_color = "black"
        top_color = "black"
        bottom_color = "black"

        if not self.has_left_wall:
            left_color = "white"

        if not self.has_right_wall:
            right_color = "white"

        if not self.has_top_wall:
            top_color = "white"

        if not self.has_bottom_wall:
            bottom_color = "white"

        self._win.draw_line(left_wall, left_color)
        self._win.draw_line(right_wall, right_color)
        self._win.draw_line(top_wall, top_color)
        self._win.draw_line(bottom_wall, bottom_color)

    def draw_move(self, to_cell, undo=False):
        x1, y1 = self.find_center()
        x2, y2 = to_cell.find_center()
        line = Line(Point(x1, y1), Point(x2, y2))
        fill_color = "red"

        if undo:
            fill_color = "gray"

        self._win.draw_line(line, fill_color)

    def find_center(self):
        center_x = abs((self._x1 + self._x2) // 2)
        center_y = abs((self._y1 + self._y2) // 2)

        return center_x, center_y
