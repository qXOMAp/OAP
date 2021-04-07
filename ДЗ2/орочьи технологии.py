print('Waaagh!')

# Вводим начальные данные

from Input import get_input

EF1, EF2, EF3, C1, C2, F1, F2 = get_input()

# Составляем матрицу жесткости
from matrix import matrix

K = matrix(EF1, EF2, EF3, C1, C2)
print('Waaagh!')
print("Матрица жескости до введения ГУ" + "\n" + "K:", K)

# Граничные условия
from border_conditions import border_condition

K = border_condition(K)
print('Waaagh!')
print("Матрица жескости после введения ГУ" + "\n" + "K:", K)

# Вектор внешних узловых увилий:
f = [0, F1, 0, F2, 0, 0]

from matan import inverse_matrix

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


print('Waaagh!')

import first_node_per

first_node_per.per(q[0], q[1])

print('Waaagh!')

import second_node_per

second_node_per.per(q[1], q[2])

print('Waaagh!')

import third_node_per

third_node_per.per(q[2], q[3])

print('Waaagh!')

import first_pr_per

first_pr_per.per(q[4], q[1])

print('Waaagh!')

import second_pr_per

second_pr_per.per(q[2], q[5])

print('Waaagh!')

# Внутренние усилия в стержне:
# N = EFu'


import first_node_force

first_node_force.force(q[0], q[1], EF1)

print('Waaagh!')

import second_node_force

second_node_force.force(q[1], q[2], EF2)

print('Waaagh!')

import third_node_force

third_node_force.force(q[2], q[3], EF3)

print('Waaagh!')

import first_pr_force

first_pr_force.force(q[4], q[1], C1)

print('Waaagh!')

import second_pr_force

second_pr_force.force(q[2], q[5], C2)

print('Waaagh!')
