from math import log, e, sqrt

import sympy


def bisection_method(func, interval, epsilon):
    a, b = interval
    n = 1
    while b - a > 2 * epsilon:
        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2

        if func(x1) > func(x2):
            a = x1
        else:
            b = x2
        n += 1

    return (a + b) / 2, func((a + b) / 2)


def golden_section_search(f, a, b, tol=1e-5):
    gr = (sqrt(5) + 1) / 2  # Золотое сечение

    x1 = b - (b - a) / gr
    x2 = a + (b - a) / gr

    while abs(x1 - x2) > tol:
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / gr
        x2 = a + (b - a) / gr

    return (a + b) / 2, f((a + b) / 2)


def chord_method(f, a, b, tol=1e-5):
    x_sym = sympy.symbols("x")
    expr = f(x_sym)
    diff_expr = sympy.diff(expr, x_sym)

    while True:
        x = a - (a - b) * (diff_expr.subs(x_sym, a) /
                           (diff_expr.subs(x_sym, a) - (diff_expr.subs(x_sym, b))))
        if abs(diff_expr.subs(x_sym, x)) > tol:
            if diff_expr.subs(x_sym, x) > 0:
                b = x
            else:
                a = x
        else:
            return float(x), float(f(x))


def newton_method(func, interval, epsilon):
    a, b = interval
    x_sym = sympy.symbols("x")
    expr = func(x_sym)
    diff1_expr = sympy.diff(expr, x_sym)
    diff2_expr = sympy.diff(diff1_expr, x_sym)
    x_prev = a
    while True:
        x_cur = x_prev - (diff1_expr.subs(x_sym, x_prev) / diff2_expr.subs(x_sym, x_prev))
        if diff1_expr.subs(x_sym, x_cur) <= epsilon:
            return x_cur, func(x_cur)
        else:
            x_prev = x_cur


print(bisection_method(
    lambda x: (1 / 3) * x ** 3 - 5 * x + log(x, e) * x,
    [1.5, 2],
    0.02))

print(golden_section_search(
    lambda x: (1 / 3) * x ** 3 - 5 * x + log(x, e) * x,
    1.5, 2,
    0.02))

print(chord_method(
    lambda x: (1 / 3) * x ** 3 - 5 * x + sympy.log(x, e) * x,
    1.5, 2,
    0.02))

print(newton_method(
    lambda x: (1 / 3) * x ** 3 - 5 * x + sympy.log(x, e) * x,
    [1.5, 2],
    0.02))
