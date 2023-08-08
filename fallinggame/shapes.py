import math


def is_between(value, minimum, maximum):
    return minimum <= value <= maximum


class Point:

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __str__(self) -> str:
        return "(" + self._x + ", " + self._y + ")"

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 +
                         (p1.y - p2.y)**2)


class Rectangle:
    def __init__(self, x, y, width, height) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self) -> str:
        return "(" + str(self._x) + "," + \
               str(self._y) + "," + \
               str(self._width) + "," + \
               str(self._height)+")"

    def draw(self, canvas):
        canvas.create_rectangle(self._x, self._y,
                                self._x + self._width,
                                self._y + self._height,
                                fill='green')

    @property
    def left(self):
        return self._x

    @left.setter
    def left(self, value):
        self._x = value

    @property
    def top(self):
        return self._y

    @top.setter
    def top(self, value):
        self._y = value

    @property
    def right(self):
        return self._x + self._width

    @right.setter
    def right(self, value):
        self._x = value - self._width

    @property
    def bottom(self):
        return self._y + self._height

    @bottom.setter
    def bottom(self, value):
        self._y = value - self._height

    @property
    def top_left(self):
        return Point(self.left, self.top)

    @property
    def top_right(self):
        return Point(self.right, self.top)

    @property
    def bottom_left(self):
        return Point(self.left, self.bottom)

    @property
    def bottom_right(self):
        return Point(self.right, self.bottom)

    def contains(self, point):
        return is_between(point.x, self.left, self.right) \
               and is_between(point.y, self.top, self.bottom)

    def contains_rect(self, rect):
        return self.contains(rect.top_left) and \
            self.contains(rect.top_right) and \
            self.contains(rect.bottom_right) and \
            self.contains(rect.bottom_left)

    def intersects(self, rect):
        return not(rect.left > self.right or
                   rect.right < self.left or
                   rect.top > self.bottom or
                   rect.bottom < self.top)





class Star:
    def __init__(self, x, y, p, d) -> None:
        self._x = x
        self._y = y
        self._p = p
        self._d = d
        self._points = [(x, y-p), (x+d, y-d), (x+p, y),
                        (x+d, y+d), (x, y+p),
                        (x-d, y+d), (x-p, y), (x-d, y-d)]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        self._p = value

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value

    def draw(self, canvas):
        canvas.create_polygon(self._points,
                              outline='black',
                              fill='yellow',
                              width=1)



