# Модуль вывода перемещений 2 узла


from Aproxima import approximation


def per(q1, q2):
    print("Перемещения для второго элемента")
    print("0   ", approximation(0, [q1, q2], 1))
    print("0.25", approximation(0.25, [q1, q2], 1))
    print("0.5 ", approximation(0.5, [q1, q2], 1))
    print("0.75", approximation(0.75, [q1, q2], 1))
    print("1   ", approximation(1, [q1, q2], 1))
