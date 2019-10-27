from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, width, height):
        self._width = width
        self._height = height
        self._fc = FigureColor()
        self._fc.color = color

    def area(self):
        return self._width * self._height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self._fc.color,
            self._width,
            self._height,
            self.area()
        )
