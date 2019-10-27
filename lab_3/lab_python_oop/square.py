from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, side):
        self._side = side
        super().__init__(color, self._side, self._side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self._fc.color,
            self._side,
            self.area()
        )
