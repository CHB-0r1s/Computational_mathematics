import sympy as sp


def bisection_method(func, interval, epsilon):
    a, b = interval
    n = 1
    while True:
        x = (a + b) / 2
        if func(a) * func(x) > 0:
            a = x
        else:
            b = x

        if abs(a - b) <= epsilon or abs(func(x)) < epsilon:
            return (a + b) / 2, func((a + b) / 2), n
        else:
            n += 1


def simple_iterations_method(func, interval, epsilon):
    n = 1
    x_sym = sp.symbols('x')
    lm = sp.symbols('lambda')
    a, b = interval

    start_expr = func(x_sym)
    s_e_diff = sp.diff(start_expr, x_sym)

    phi = x_sym + lm * start_expr

    expr_diff_a = abs(s_e_diff.subs(x_sym, a))
    expr_diff_b = abs(s_e_diff.subs(x_sym, b))

    lm_res = (-1 / max(expr_diff_a, expr_diff_b))

    phi_res = phi.subs(lm, lm_res)

    def is_convergence() -> (bool, int):
        phi_res_diff = sp.diff(phi_res, x_sym)

        a_res = phi_res_diff.subs(x_sym, a)
        b_res = phi_res_diff.subs(x_sym, b)

        q_ = max(a_res, b_res)

        return q_ < 1, q_

    is_conv, q = is_convergence()
    if not is_conv:
        print(f"Не сходится. q = {q}")
        return None

    x_prev = a
    x_cur = phi_res.subs(x_sym, x_prev)

    while abs(x_cur - x_prev) > epsilon:
        x_prev = x_cur
        x_cur = phi_res.subs(x_sym, x_prev)
        n += 1

    return x_cur, func(x_cur), n


def newton_method(func, interval, epsilon):
    pass
