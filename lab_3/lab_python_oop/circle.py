from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, radius):
        self._radius = radius
        self._fc = FigureColor()
        self._fc.color = color

    def area(self):
        return math.pi * (self._radius ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self._fc.color,
            self._radius,
            self.area()
        )
