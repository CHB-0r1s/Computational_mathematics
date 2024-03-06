import numpy as np

#f"Введите {q+1}-ую строчку A через пробел: "
n = int(input("Введите размерность матрицы: "))

A: list[list] = [
    list(map(float, input().split()))
    for q in range(n)
]
B: list = list(map(float, input("Введите B^T (вектор-строчку) через пробел: ").split()))

X: list = [0 for _ in range(n)]
D: float = round(np.linalg.det(np.array(A)), 5)

if not all([len(elem) == n for elem in A]):
    raise Exception("Ошибка ввода матрицы А")

if len(B) != n:
    raise Exception("Ошибка ввода матрицы B")

print("Введённая матрица A:")
print(np.array(A))
print("Введённая матрица B^T:")
print(f"{B}")

print("Определитель матрицы:")
print(f"D = {D}")

if D == 0:
    raise Exception(
        "D = 0, у системы либо нет решений, либо бесконечно много. Не удовлетворяет критерию меода Гаусса "
    )

for i in range(1, n):
    if A[i - 1][i - 1] == 0:
        # swap строк
        for _ in range(n):
            A = [A[-1]] + A[:-1]
            if A[i - 1][i - 1] == 0:
                break
        else:
            raise Exception("Система не решаема")
    for k in range(i + 1, n + 1):
        c = A[k - 1][i - 1] / A[i - 1][i - 1]
        A[k - 1][i - 1] = 0

        for j in range(i + 1, n + 1):
            A[k - 1][j - 1] = A[k - 1][j - 1] - (c * A[i - 1][j - 1])
        B[k - 1] = B[k - 1] - c * B[i - 1]

print("Матрица A в треугольном виде:")
print(np.array(A))
print("Матрица B^T после изменений:")
print(B)

for i in range(n, 0, -1):
    s = 0
    for j in range(i + 1, n + 1):
        s += A[i - 1][j - 1] * X[j - 1]

    X[i - 1] = (B[i - 1] - s) / A[i - 1][i - 1]

print("X-матрица")
print(X)
"""
3
10 -7 0
-3 2 6
5 -1 5
7 4 6
"""

R = [sum([A[i][j] * X[j] for j in range(n)]) - B[i] for i in range(n)]

print("Невязки: ")
print(R)
