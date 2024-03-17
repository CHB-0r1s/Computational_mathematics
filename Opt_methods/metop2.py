import time


def square_approx(f, x1_, delta_x, e1, e2):
    need2 = True
    x1 = x1_
    while True:
        if need2:
            x2 = x1 + delta_x
            f_x1 = f(x1)
            f_x2 = f(x2)
            if f_x1 > f_x2:
                x3 = x1 + 2 * delta_x
            else:
                x3 = x1 - delta_x

        f_x1 = f(x1)
        f_x2 = f(x2)
        f_x3 = f(x3)
        F_min = min(f_x1, f_x2, f_x3)
        x_min = [x1, x2, x3][[f_x1, f_x2, f_x3].index(F_min)]
        print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
        print(f"f1 = {f_x1}, f2 = {f_x2}, f3 = {f_x3}")
        print(f"F_min = {F_min}")
        print(f"x_min = {x_min}")
        print(f_x1, f_x2, f_x3)
        time.sleep(1)

        if ((x2 - x3) * f_x1 + (x3 - x1) * f_x2 + (x1 - x2) * f_x3) == 0:
            print(f"Знаменатель обращается в 0. x1 = x_min: x1 = {x_min}")
            print("+-----------------+")
            x1 = x_min
            need2 = True
            continue

        x_ = (0.5 *
              ((x2 ** 2 - x3 ** 2) * f_x1 + (x3 ** 2 - x1 ** 2) * f_x2 + (x1 ** 2 - x2 ** 2) * f_x3) /
              ((x2 - x3) * f_x1 + (x3 - x1) * f_x2 + (x1 - x2) * f_x3))

        f_x_ = f(x_)
        print(f"x_ = {x_}")
        print(f"f_ = {f_x_}")
        time.sleep(1)

        if abs((F_min - f_x_) / f_x_) < e1 and abs((x_min - x_) / x_) < e2:
            print("Условие завершения итерации выполнено")
            print(f"Ответ: {x_}")
            return x_
        else:
            if x1 <= x_ <= x3:
                x1_new, x2_new, x3_new = x1, x2, x3
                if x_min == x1:
                    x1_new = x1
                    x2_new = x_min
                    x3_new = min(x_, x2, x3)
                elif x_min == x2:
                    if x_ > x2:
                        x1_new = x2
                        x2_new = x_
                        x3_new = x3

                    elif x_ < x2:
                        x1_new = x1
                        x2_new = x_
                        x3_new = x2
                elif x_min == x3:
                    x1_new = max(x1, x2, x_)
                    x2_new = x_min
                    x3_new = x3
                x1 = x1_new
                x2 = x2_new
                x3 = x3_new
                need2 = False
                print(f"Новые x: x1 = {x1_new}, x2 = {x2_new}, x3 = f{x3_new}")
            else:
                x1 = x_
                need2 = True
        print(f"Конец итерации: x1 = {x1}, x2 = {x2}, x3 = {x3}, x_ = {x_}")
        print("+-----------------+")


func = lambda x: 2 * x ** 2 + 16 / x
print(square_approx(func, 1, 1, 0.003, 0.03))
