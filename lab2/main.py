from nlin_eq_solve_methods import *

'''
# f_state = input("Хотите посчитать уравнение(1) или систему(2)? [1, 2] ")
# if f_state in ["1", "2"]:
#     if f_state == "1":
#         text_func = input("Вводите функцию. Переменная x (пример x^2 + 2 * x + 1): ")
#         if (
#                 len([char for char in text_func if char.isalpha()]) and
#                 len([char for char in text_func if char.isalnum()]) and
#                 len([char for char in text_func if char.isalpha()]) == text_func.count("x")
#         ):
#             text_func = text_func.replace('^', '**')
# 
#             func = lambda x: x
#             exec(f"func = lambda x: {text_func}")
# 
#             intervals = input("Введите интервал. Надо вводить как можно более строгое ограничение (пример 1 2): ")
#             if " " in intervals and len(intervals.split()) == 2:
#                 interval = [float(a) for a in intervals.split()]
# 
#                 print("Каким методом посчитать?")
#                 method_type = input("бисекции(1), Ньютона(2),  простых итераций(3) [1, 2, 3] ")
#                 if method_type in ["1", "2", "3"]:
#                     if method_type == "1":
#                         print(bisection_method(func, interval, 10 ** -4))
#                     elif method_type == "2":
#                         print(newton_method(func, interval, 10 ** -4))
#                     else:
#                         print(simple_iterations_method(func, interval, 10 ** -4))
#                 else:
#                     print("Промазали по клавише. Потренируйтесь-ка попадать.")
#             else:
#                 print("Почти получилось, надо научиться считать до двух")
#         else:
#             print("Чото в вводе не хватает :( Возможно платной подписки на доп функции ввода!")
#     else:
#         text_func_1 = input("Вводите первую функцию. Переменная x, y (пример x^2 + 2 * y + 1): ")
#         text_func_2 = input("Вводите вторую функцию. Переменная x, y (пример y^2 + 2 * x + 1): ")
#         if (
#                 len([char for char in text_func_1 if char.isalpha()]) and
#                 len([char for char in text_func_1 if char.isalnum()]) and
#                 len([char for char in text_func_1 if char.isalpha()]) ==
#                 text_func_1.count("x") + text_func_1.count("y") and
#                 len([char for char in text_func_2 if char.isalpha()]) and
#                 len([char for char in text_func_2 if char.isalnum()]) and
#                 len([char for char in text_func_2 if char.isalpha()]) ==
#                 text_func_2.count("x") + text_func_2.count("y")
#         ):
#             text_func_1 = text_func_1.replace('^', '**')
#             text_func_2 = text_func_2.replace('^', '**')
# 
#             func1 = lambda x, y: x + y
#             exec(f"func1 = lambda x, y: {text_func_1}")
# 
#             func2 = lambda x, y: x + y
#             exec(f"func2 = lambda x, y: {text_func_2}")
# 
#             intervals_1 = input("Введите интервал для x."
#                                 " Надо вводить как можно более строгое ограничение (пример 1 2): ")
#             intervals_2 = input("Введите интервал для y."
#                                 " Надо вводить как можно более строгое ограничение (пример 1 2): ")
# 
#             if (" " in intervals_1 and len(intervals_1.split()) == 2
#                     and " " in intervals_2 and len(intervals_2.split()) == 2):
#                 interval_1 = [float(a) for a in intervals_1.split()]
#                 interval_2 = [float(a) for a in intervals_2.split()]
# 
#                 print(simple_iterations_method_for_system_2(func1, func2, [interval_1, interval_2], 10 ** -2))
#             else:
#                 print("Почти получилось, надо научиться считать до двух")
#         else:
#             print("Чото в вводе не хватает :( Возможно платной подписки на доп функции ввода!")
# 
# 
# else:
#     print("Ну и ладно")

'''

