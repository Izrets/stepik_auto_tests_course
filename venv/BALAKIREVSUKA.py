# def func_show(func):
#     def show_text(*args, **kwargs):
#         print(f'Площадь прямоугольника: {*args * **kwargs}')
#     return show_text
#
# @func_show
# def get_sq(width, height):
#     return width, height
#
# get_sq()



def func_decorator(func):
    def wrapper():
        print('sadasd')
        print(func())
        print('sdgggggg')
    return wrapper

@func_decorator
def some_func():
    return ('ХУЙ')

some_func()


