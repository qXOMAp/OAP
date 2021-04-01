print('Waaagh!')

# Жёсткости элементов
EF1 = 6
EF2 = 7
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
print('K', K)

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
print(K)

# Вектор внешних узловых увилий:
f = [0, F1, 0, F2, 0, 0]

from module import inverse_matrix

invK = inverse_matrix(K)
print('Waaagh!')
print(invK)

q = []
for i in range(len(f)):
    u = 0
    for j in range(len(f)):
        u += invK[i][j] * f[j]
    q.append(u)
print('Waaagh!')
print(q)

#Апроксимации
