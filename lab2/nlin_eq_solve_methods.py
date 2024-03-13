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

    if s_e_diff.subs(x_sym, a) > 0:
        lm_res = -1 / max(expr_diff_a, expr_diff_b)
    else:
        lm_res = 1 / max(expr_diff_a, expr_diff_b)

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

    return float(x_cur), float(func(x_cur)), n


def newton_method(func, interval, epsilon):
    a, b = interval
    x_sym = sp.symbols('x')
    n = 1
    start_expr = func(x_sym)

    s_e_diff_1 = sp.diff(start_expr, x_sym)
    s_e_diff_2 = sp.diff(s_e_diff_1, x_sym)

    if start_expr.subs(x_sym, a) * s_e_diff_2.subs(x_sym, a) > 0:
        x_prev = a
    else:
        x_prev = b

    x_cur = x_prev - start_expr.subs(x_sym, x_prev) / s_e_diff_1.subs(x_sym, x_prev)
    while abs(x_cur - x_prev) > epsilon:
        x_prev, x_cur = x_cur, x_prev - start_expr.subs(x_sym, x_prev) / s_e_diff_1.subs(x_sym, x_prev)
        n += 1
    res = x_prev - start_expr.subs(x_sym, x_prev) / s_e_diff_1.subs(x_sym, x_prev)
    return round(res, 3), round(func(res), 3), n


def simple_iterations_method_for_system_2(func1, func2, intervals, epsilon):
    n = 1
    x1_sym = sp.symbols('x_1')
    x2_sym = sp.symbols('x_2')

    lm_1 = sp.symbols('lambda_1')
    lm_2 = sp.symbols('lambda_2')

    x_1_lower_bound, x_1_upper_bound = intervals[0]
    x_2_lower_bound, x_2_upper_bound = intervals[1]

    start_expr_1 = func1(x1_sym, x2_sym)
    start_expr_2 = func2(x1_sym, x2_sym)

    phi_1 = x1_sym + lm_1 * start_expr_1
    phi_2 = x2_sym + lm_2 * start_expr_2

    s_e_1_diff_x1 = sp.diff(start_expr_1, x1_sym)
    s_e_1_diff_x2 = sp.diff(start_expr_1, x2_sym)
    s_e_1_diff_G = [s_e_1_diff_x1.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_lower_bound),
                    s_e_1_diff_x1.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_upper_bound),
                    s_e_1_diff_x1.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_lower_bound),
                    s_e_1_diff_x1.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_upper_bound),
                    s_e_1_diff_x2.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_lower_bound),
                    s_e_1_diff_x2.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_upper_bound),
                    s_e_1_diff_x2.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_lower_bound),
                    s_e_1_diff_x2.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_upper_bound)]
    lm_phi_1 = max(s_e_1_diff_G)
    phi_1 = phi_1.subs(lm_1, -1 / lm_phi_1)

    s_e_2_diff_x1 = sp.diff(start_expr_2, x1_sym)
    s_e_2_diff_x2 = sp.diff(start_expr_2, x2_sym)
    s_e_2_diff_G = [
        s_e_2_diff_x1.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_lower_bound),
        s_e_2_diff_x1.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_upper_bound),
        s_e_2_diff_x1.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_lower_bound),
        s_e_2_diff_x1.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_upper_bound),
        s_e_2_diff_x2.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_lower_bound),
        s_e_2_diff_x2.subs(x1_sym, x_1_lower_bound).subs(x2_sym, x_2_upper_bound),
        s_e_2_diff_x2.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_lower_bound),
        s_e_2_diff_x2.subs(x1_sym, x_1_upper_bound).subs(x2_sym, x_2_upper_bound)
    ]
    lm_phi_2 = max(s_e_2_diff_G)
    phi_2 = phi_2.subs(lm_2, -1 / lm_phi_2)
    # phi_2 = -1 * (3 * (x1_sym ** 3) + 2)

    if (
            bool(
                abs(sp.diff(phi_1, x1_sym).subs(x1_sym, x_1_upper_bound - epsilon).subs(x2_sym, x_2_upper_bound)) +
                abs(sp.diff(phi_1, x2_sym).subs(x2_sym, x_2_upper_bound + epsilon).subs(x1_sym, x_1_upper_bound)) < 1
            )
            and
            bool(
                abs(sp.diff(phi_2, x1_sym).subs(x1_sym, x_1_upper_bound - epsilon).subs(x2_sym, x_2_upper_bound)) +
                abs(sp.diff(phi_2, x2_sym).subs(x2_sym, x_2_upper_bound).subs(x1_sym, x_1_upper_bound - epsilon)) < 1
            )
    ):
        print("Не сходиться! Задайте интервалы более строго.")
        return None

    x1_prev = x_1_upper_bound
    x2_prev = x_2_upper_bound

    x1_cur = phi_1.subs(x1_sym, x1_prev).subs(x2_sym, x2_prev)
    x2_cur = phi_2.subs(x1_sym, x1_prev).subs(x2_sym, x2_prev)

    while abs(x1_cur - x1_prev) > epsilon or abs(x2_cur - x2_prev) > epsilon:
        x1_prev = x1_cur
        x1_cur = phi_1.subs(x1_sym, x1_prev).subs(x2_sym, x2_prev)

        x2_prev = x2_cur
        x2_cur = phi_2.subs(x1_sym, x1_prev).subs(x2_sym, x2_prev)
        n += 1

    return (x1_cur, x2_cur), start_expr_1.subs(x1_sym, x1_cur).subs(x2_sym, x2_cur), n


print(simple_iterations_method_for_system_2(
    lambda x, y: 2 * x ** 2 - y - 5,
    lambda x, y: 3 * x ** 3 + y + 2,
    [[0.1, 0.83], [-4, -3.5]],
    10 ** -5
))
