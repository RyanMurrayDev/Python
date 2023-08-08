from shapes import *
from tkinter import *
import math
from datetime import datetime


class Sprite(Rectangle):
    def __init__(self, x, y, width, height) -> None:
        super().__init__(x, y, width, height)

    def increment_x(self, distance):
        self._x += distance

    def increment_y(self, distance):
        self._y += distance


class ImageSprite(Sprite):
    def __init__(self, imageObj, x, y) -> None:
        super().__init__(x, y, imageObj.width(),
                         imageObj.height())
        self._image = imageObj

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def draw(self, canvas):
        canvas.create_image(self.x, self.y,
                            anchor=NW,
                            image=self._image)


class HorizontalBouncer(ImageSprite):

    def __init__(self, image_obj, x, y, minimum,
                 maximum, distance, update_time) -> None:
        super().__init__(image_obj, x, y)
        self._minimum = minimum
        self._maximum = maximum
        self._distance = distance
        self._elapsed_time = 0
        self._update_time = update_time

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    @property
    def direction(self):
        if self._distance <= 0:
            return "left"
        else:
            return "right"

    @direction.setter
    def direction(self, value):
        if value == "left":
            self._distance = -1 * abs(self._distance)
        else:
            self._distance = abs(self._distance)

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value

    def update(self, delta_time):
        self._elapsed_time += delta_time
        if self._elapsed_time >= self._update_time:
            self._elapsed_time = 0
            self.increment_x(self._distance)
            if self.left < self._minimum:
                self.left = self._minimum
                self._distance *= -1

            elif self.right > self._maximum:
                self.right = self._maximum
                self._distance *= -1


class VerticalRepeater(ImageSprite):

    def __init__(self, image_obj, x, y, minimum,
                 maximum, distance, update_time) -> None:
        super().__init__(image_obj, x, y)
        self._minimum = minimum
        self._maximum = maximum
        self._distance = distance
        self._elapsed_time = 0
        self._update_time = update_time

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    @property
    def direction(self):
        if self._distance <= 0:
            return "left"
        else:
            return "right"

    @direction.setter
    def direction(self, value):
        if value == "left":
            self._distance = -1 * abs(self._distance)
        else:
            self._distance = abs(self._distance)

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value

    def update(self, delta_time):
        self._elapsed_time += delta_time
        if self._elapsed_time >= self._update_time:
            self._elapsed_time = 0
            self.increment_y(self._distance)
            if self.bottom > self._maximum:
                self.bottom = self._minimum

class HorizontalMover(ImageSprite):

    def __init__(self, image_obj, x, y, minimum,
                 maximum, distance, update_time) -> None:
        super().__init__(image_obj, x, y)
        self._minimum = minimum
        self._maximum = maximum
        self._distance = distance
        self._elapsed_time = 0
        self._update_time = update_time

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    @property
    def direction(self):
        if self._distance <= 0:
            return "left"
        else:
            return "right"

    @direction.setter
    def direction(self, value):
        if value == "left":
            self._distance = -1 * abs(self._distance)
        else:
            self._distance = abs(self._distance)

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value

    def update(self, delta_time):
        self._elapsed_time += delta_time
        if self._elapsed_time >= self._update_time:
            self._elapsed_time = 0
            self.increment_x(self._distance)
            if self.left < self._minimum:
                self.left = self._minimum

            elif self.right > self._maximum:
                self.right = self._maximum