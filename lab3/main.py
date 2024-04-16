from numpy import sin
from numpy import arange


def Runge_method(k):
    def Runge(method):
        def wrapper(f, a, b, n):
            res = (method(f, a, b, n * 2) - method(f, a, b, n)) / ((2 ** k) - 1)
            print(f"Runge: {res}")
            return method(f, a, b, n)

        return wrapper

    return Runge


@Runge_method(k=2)
def pr_left_method(func, a, b, n):
    h = (b - a) / n
    return sum([h * func(x) for x in arange(a, b, h)])


@Runge_method(k=2)
def pr_right_method(func, a, b, n):
    h = (b - a) / n
    return sum([h * func(x) for x in arange(a + h, b, h)] + [h * func(b)])


@Runge_method(k=2)
def pr_middle_method(func, a, b, n):
    h = (b - a) / n
    return sum([h * func(x + h / 2) for x in arange(a, b, h)])


@Runge_method(k=2)
def trap_method(func, a, b, n):
    h = (b - a) / n
    return (h / 2) * (func(a) + func(b) + 2 * sum([func(x) for x in arange(a + h, b, h)]))


@Runge_method(k=4)
def simson_method(func, a, b, n):
    h = (b - a) / n
    return (h / 3) * (func(a) + func(b) +
                      4 * sum([func(x) for x in arange(a + h, b, 2 * h)]) +
                      2 * sum([func(x) for x in arange(a + 2 * h, b - h, 2 * h)]))



f_input = lambda x: x
text_func = input("Вводите функцию. Переменная x (пример x^2 + 2 * x + 1): ")
text_func = text_func.replace('^', '**')
exec(f"f_input = lambda x: {text_func}")

a_input = float(input("Граница а = "))
b_input = float(input("Граница b = "))
n_input = int(input("n = "))

method_input = input("Введите номер метода [1 (лев), 2 (сред), 3 (прав), 4 (трап), 5 (Симпсона), 0 (нет настроения)] ")
if method_input == '0':
    print("Сочувствую")
elif method_input == '1':
    print(f"Результат {pr_left_method(f_input, a_input, b_input, n_input)}")
elif method_input == '2':
    print(f"Результат {pr_middle_method(f_input, a_input, b_input, n_input)}")
elif method_input == '3':
    print(f"Результат {pr_right_method(f_input, a_input, b_input, n_input)}")
elif method_input == '4':
    print(f"Результат {trap_method(f_input, a_input, b_input, n_input)}")
elif method_input == '5':
    print(f"Результат {simson_method(f_input, a_input, b_input, n_input)}")
else:
    print("ну введите правильно в след раз блин")
