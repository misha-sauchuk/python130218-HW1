"""Реализовать модуль, содержащий следующие функции декораторы:
декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции
"""
# import modules to calculate time and to use decorator @functools.wraps() to save func attr(__doc__,
# __name__, __module__, etc) after the decoration
import time
import functools


# декоратор, позволяющий вместе с результатом функции возвращать время ее работы
def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        star_time = time.time()
        result_func = func(*args, **kwargs)
        result_time = time.time()-star_time
        print('The result of func is {}\n'
              'and it is necessary {} sec to calculate it'.format(result_func, result_time))
        return func
    return inner


# декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл
def log_timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        with open('log_file.txt', 'a') as log:
            star_time = time.time()
            func(*args, **kwargs)
            result_time = (time.time() - star_time)
            print(func.__name__, str(args), str(kwargs), str("%.5f" % result_time), sep=' | ', file=log)
        return func
    return inner


# декоратор, проверяющий типы, переданных декорируемой функции, аргументов
def type_arg(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        for arg in args:
            print(type(arg))
        for kwarg in kwargs.values():
            print(type(kwarg))
        return func
    return inner


# декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции
def cache(func):
    cache_data = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs))
        if key not in cache_data:
            cache_data[key] = func(*args, **kwargs)
        return cache_data[key]
    return inner


# test our decorations if file loads as main file (not module)
if __name__ == '__main__':
    @timer
    def timer_sum():
        return sum(i for i in range(5 ** 10))

    @log_timer
    def great_sum(num):
        return sum(i for i in range(num ** 10))

    @type_arg
    def func_args(*args, **kwargs):
        print(args, kwargs)

    @cache
    def initialize_settings(file_name):
        with open(file_name) as file:
            file.read()
        print('this function load file "{}" only one time'.format(file_name))

    timer_sum()
    great_sum(5)
    func_args(1, 2, 3, x='1', y=[1, 2, 3])
    initialize_settings('students_info.txt')
    initialize_settings('students_info.txt')
    initialize_settings('log_file.txt')
    initialize_settings('students_info.txt')
