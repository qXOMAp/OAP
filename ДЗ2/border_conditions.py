def border_condition(K):
    # Граничные условия, примененные к глобальной матрице жесткости системы:
    K[0][0] = 1
    for i in range(1, len(K[0])):
        K[0][i] = 0

    for i in range(1, len(K)):
        K[i][0] = 0

    for i in range(0, 5):
        K[5][i] = 0
    for i in range(0, 5):
        K[i][5] = 0
    K[5][5] = 1
    return K
