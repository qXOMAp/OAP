print('Waaagh!')

# Жёсткости элементов
EF1 = 6
EF2 = 4
EF3 = 8
C1 = 1
C2 = 2

# Внеешние усилия
F1 = 10
F2 = 20

# Составляем матрицу жесткости
K1 = [[EF1, -EF1],
      [-EF1, EF1]]
K2 = [[EF2, -EF2],
      [-EF2, EF2]]
K3 = [[EF3, -EF3],
      [-EF3, EF3]]
K4 = [[C1, -C1],
      [-C1, C1]]
K5 = [[C2, -C2],
      [-C2, C2]]

print("K1:", K1)
print("K2:", K2)
print("K3:", K3)
print("K4:", K4)
print("K5:", K5)

K = [[K1[0][0], K1[0][1], 0, 0, 0, 0],
     [K1[1][0], K1[1][1] + K2[0][0] + K4[1][1], K2[0][1], 0, K4[1][0], 0],
     [0, K2[1][0], K2[1][1] + K3[0][0] + K5[1][1], K3[0][1], 0, K5[0][1]],
     [0, 0, K3[1][0], K3[1][1], 0, 0],
     [0, K4[0][1], 0, 0, K4[0][0], 0],
     [0, 0, K5[1][0], 0, 0, K5[1][1]]]

print('Waaagh!')
print('Матрица жесткости', K)

# Граничные условия
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
print('Waaagh!')
print('Граничные условия', K)

# Вектор внешних узловых увилий:
f = [0, F1, 0, F2, 0, 0]

from module import inverse_matrix

invK = inverse_matrix(K)
print('Waaagh!')
print('обратная', invK)

q = []
for i in range(len(f)):
    u = 0
    for j in range(len(f)):
        u += invK[i][j] * f[j]
    q.append(u)
print('Waaagh!')
print('u', q)


# Апроксимации
def scalar_product(a, b):
    return a[0] * b[0] + a[1] * b[1]


def approximation(x, u, l):
    N1 = 1 - x / l
    N2 = x / l
    N = [N1, N2]
    return scalar_product(N, u)


print('Waaagh!')

print("Перемещения для первого элемента")
print("0", approximation(0, [q[0], q[1]], 1))
print("0.25", approximation(0.25, [q[0], q[1]], 1))
print("0.5", approximation(0.5, [q[0], q[1]], 1))
print("0.75", approximation(0.75, [q[0], q[1]], 1))
print("1", approximation(1, [q[0], q[1]], 1))

print('Waaagh!')

print("Перемещения для фторого элемента")
print("0", approximation(0, [q[1], q[2]], 1))
print("0.25", approximation(0.25, [q[1], q[2]], 1))
print("0.5", approximation(0.5, [q[1], q[2]], 1))
print("0.75", approximation(0.75, [q[1], q[2]], 1))
print("1", approximation(1, [q[1], q[2]], 1))

print('Waaagh!')

print("Перемещения для третьего элемента")
print("0", approximation(0, [q[2], q[3]], 1))
print("0.25", approximation(0.25, [q[2], q[3]], 1))
print("0.5", approximation(0.5, [q[2], q[3]], 1))
print("0.75", approximation(0.75, [q[2], q[3]], 1))
print("1", approximation(1, [q[2], q[3]], 1))

print('Waaagh!')

print("Перемешения для перфой пружины")
print("0", approximation(0, [q[4], q[1]], 1))
print("0.25", approximation(0.25, [q[4], q[1]], 1))
print("0.5", approximation(0.5, [q[4], q[1]], 1))
print("0.75", approximation(0.75, [q[4], q[1]], 1))
print("1", approximation(1, [q[4], q[1]], 1))

print('Waaagh!')

print("Перемешения для фторой пружины")
print("0", approximation(0, [q[2], q[5]], 1))
print("0.25", approximation(0.25, [q[2], q[5]], 1))
print("0.5", approximation(0.5, [q[2], q[5]], 1))
print("0.75", approximation(0.75, [q[2], q[5]], 1))
print("1", approximation(1, [q[2], q[5]], 1))

print('Waaagh!')


# Внутренние усилия в стержне:
# N = EFu'


def force_approximation(x, u, l, EF):
    N1prime = -1 / l
    N2prime = 1 / l
    N = [N1prime, N2prime]
    return scalar_product(N, u) * EF


print("Усилия для первого элемента")
print("0", force_approximation(0, [q[0], q[1]], 1, EF1))
print("0.25", force_approximation(0.25, [q[0], q[1]], 1, EF1))
print("0.5", force_approximation(0.5, [q[0], q[1]], 1, EF1))
print("0.75", force_approximation(0.75, [q[0], q[1]], 1, EF1))
print("1", force_approximation(1, [q[0], q[1]], 1, EF1))

print('Waaagh!')

print("Усилия для второго элемента")
print("0", force_approximation(0, [q[1], q[2]], 1, EF2))
print("0.25", force_approximation(0.25, [q[1], q[2]], 1, EF2))
print("0.5", force_approximation(0.5, [q[1], q[2]], 1, EF2))
print("0.75", force_approximation(0.75, [q[1], q[2]], 1, EF2))
print("1", force_approximation(1, [q[1], q[2]], 1, EF2))

print('Waaagh!')

print("Усилия для третьего элемента")
print("0", force_approximation(0, [q[2], q[3]], 1, EF3))
print("0.25", force_approximation(0.25, [q[2], q[3]], 1, EF3))
print("0.5", force_approximation(0.5, [q[2], q[3]], 1, EF3))
print("0.75", force_approximation(0.75, [q[2], q[3]], 1, EF3))
print("1", force_approximation(1, [q[2], q[3]], 1, EF3))

print('Waaagh!')

print("Усилия для первой пружины")
print("0", force_approximation(0, [q[4], q[1]], 1, C1))
print("0.25", force_approximation(0.25, [q[4], q[1]], 1, C1))
print("0.5", force_approximation(0.5, [q[4], q[1]], 1, C1))
print("0.75", force_approximation(0.75, [q[4], q[1]], 1, C1))
print("1", force_approximation(1, [q[4], q[1]], 1, C1))

print('Waaagh!')

print("Усилия для фторой пружины")
print("0", force_approximation(0, [q[2], q[5]], 1, C2))
print("0.25", force_approximation(0.25, [q[2], q[5]], 1, C2))
print("0.5", force_approximation(0.5, [q[2], q[5]], 1, C2))
print("0.75", force_approximation(0.75, [q[2], q[5]], 1, C2))
print("1", force_approximation(1, [q[2], q[5]], 1, C2))

print('Waaagh!')
