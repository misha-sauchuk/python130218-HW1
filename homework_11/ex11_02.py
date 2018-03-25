"""Реализовать программу подсчета площади, периметра, объема геометрических фигур
(треугольник, прямоугольник, квадрат, трапеция, окружность).
Если одна из фигур не поддерживает вычисление одного из свойств, в программе должно быть вызвано исключение
с человеко-читабельным сообщением и корректно обработано."""

# import modules for use math methods and decorators
import math
import functools


# create decorator to catch exception in some functions
def try_deco(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except (NotImplementedError, TypeError) as er:
            print('This figure does\'t have such property\n ERROR: ', er)
        return func

    return inner


# create abstract class
class Figure:
    def square(self):  # define the function that should be complemented in subclass
        raise NotImplementedError  # raise the Exception if the function was not complemented in subclass

    def perimeter(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError

    @try_deco
    def print_square(self):
        print('The square of {fig} is {result:.2f}'.format(fig=self.name, result=self.square()))

    @try_deco
    def print_perimeter(self):
        print('The perimeter of {fig} is {result:.2f}'.format(fig=self.name, result=self.perimeter()))

    @try_deco
    def print_volume(self):
        print('The volume of {fig} is {result:.2f}'.format(fig=self.name, result=self.volume()))


# create subclass of class Figure
class Circle(Figure):
    def __init__(self, name):
        self.name = name
        self.diameter = float(input('Please, enter the diameter: '))

    def square(self):
        square = math.pi * self.diameter ** 2
        print()
        return square

    def perimeter(self):
        perimeter = math.pi * self.diameter
        return perimeter


# create subclass of class Figure
class SquareFig(Figure):
    def __init__(self, name):
        self.name = name
        self.side_a = float(input('Please, enter the side "a": '))

    def square(self):
        square = self.side_a ** 2
        return square

    def perimeter(self):
        perimeter = self.side_a * 4
        return perimeter


# create subclass of class SquareFig
class Rectangle(SquareFig):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.side_b = float(input('Please, enter the side "b": '))

    def square(self):
        square = self.side_a * self.side_b
        return square

    def perimeter(self):
        perimeter = (self.side_a + self.side_b) * 2
        return perimeter


# create subclass of class Rectangle
class Trapeze(Rectangle):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.side_c = float(input('Please, enter the side "c": '))
        self.side_d = float(input('Please, enter the side "d": '))
        self.height = float(input('Please, enter the height "h": '))
        self.check_trapeze()

    def check_trapeze(self):  # check if there is a trapeze with input values
        trap_sides = [self.side_a, self.side_b, self.side_c, self.side_d]
        max_side = max(trap_sides)
        trap_sides.pop(trap_sides.index(max_side))
        if max_side >= sum(trap_sides):
            print('There is no figure with input sizes. Please, try again.')
            self.__init__(self.name)

    def square(self):
        square = (self.side_a + self.side_b) / 2 * self.height
        return square

    def perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c + self.side_d
        return perimeter


# create subclass of class Figure
class Triangle(Figure):
    def __init__(self, name):
        self.name = name
        self.side_a = float(input('Please, enter the side "a": '))
        self.side_b = float(input('Please, enter the side "b": '))
        self.side_c = float(input('Please, enter the side "c": '))
        self.check_triangle()

    def check_triangle(self):  # check if there is a triangle with input values
        triangle_sides = [self.side_a, self.side_b, self.side_c]
        max_side = max(triangle_sides)
        triangle_sides.pop(triangle_sides.index(max_side))
        if max_side >= sum(triangle_sides):
            print('There is no figure with input sizes. Please, try again.')
            self.__init__(self.name)

    def square(self):
        p = self.perimeter() / 2
        square = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return square

    def perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter


# make request to user to input data or to exit
while True:
    figure = input('Please, choose figure:\n'  # request to input type of figure or to exit
                   '1. Circle\n'
                   '2. Square\n'
                   '3. Rectangle\n'
                   '4. Trapeze\n'
                   '5. Triangle\n'
                   '6. Exit\n')
    if figure == '1' or figure.upper() == 'CIRCLE':
        figure = Circle('Circle')
    elif figure == '2' or figure.upper() == 'SQUARE':
        figure = SquareFig('Square')
    elif figure == '3' or figure.upper() == 'RECTANGLE':
        figure = Rectangle('Rectangle')
    elif figure == '4' or figure.upper() == 'TRAPEZE':
        figure = Trapeze('Trapeze')
    elif figure == '5' or figure.upper() == 'TRIANGLE':
        figure = Triangle('Triangle')
    elif figure == '6' or figure.upper() == 'EXIT':
        break
    else:
        print('Invalid input')
        continue
    to_do = input('Please, choose what would you like to calculate:\n'  # request about operation to do with figure
                  '1. Square\n'
                  '2. Perimeter\n'
                  '3. Volume\n'
                  '4. Square & Perimeter\n')
    if to_do == '1' or to_do.upper() == 'SQUARE':
        figure.print_square()
    elif to_do == '2' or to_do.upper() == 'PERIMETER':
        figure.print_perimeter()
    elif to_do == '3' or to_do.upper() == 'VOLUME':
        figure.print_volume()
    elif to_do == '4' or to_do.upper() == 'SQUARE & PERIMETER':
        figure.print_square()
        figure.print_perimeter()


if __name__ == '__main__':

    def test_circle(name):
        fig = Circle(name)
        fig.diameter = 10
        if '{:.2f}'.format(fig.square()) == '314.16':
            print('--test_circle Ok--')

    def test_square(name):
        fig = SquareFig(name)
        fig.side_a = 10
        if '{:.2f}'.format(fig.square()) == '100.00':
            print('--test_square Ok--')

    def test_rectangle(name):
        fig = Rectangle(name)
        fig.side_a = 10
        fig.side_b = 13
        if '{:.2f}'.format(fig.perimeter()) == '46.00':
            print('--test_rectangle Ok--')

    def test_trapeze(name):
        fig = Trapeze(name)
        fig.side_a = 4
        fig.side_b = 6
        fig.side_c = 4
        fig.side_d = 3
        fig.height = 2.828
        if '{:.2f}'.format(fig.square()) == '14.14':
            print('--test_rectangle Ok--')

    def test_triangle(name):
        fig = Triangle(name)
        fig.side_a = 3
        fig.side_b = 4
        fig.side_c = 5
        if '{:.2f}'.format(fig.square()) == '6.00':
            print('--test_triangle Ok--')

    test_circle('circle_test')
    test_triangle('triangle_test')
    test_square('test_square')
    test_rectangle('test_rectangle')
    test_trapeze('test_trapeze')
