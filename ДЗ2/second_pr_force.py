# Модуль для вывода усилий 2 пружины

from Aproxima import force_approximation


def force(q1, q2, C):
    print("Усилия для второй пружины")
    print("0   ", force_approximation(0, [q1, q2], 1, C))
    print("0.25", force_approximation(0.25, [q1, q2], 1, C))
    print("0.5 ", force_approximation(0.5, [q1, q2], 1, C))
    print("0.75", force_approximation(0.75, [q1, q2], 1, C))
    print("1   ", force_approximation(1, [q1, q2], 1, C))
