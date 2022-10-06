'''
Вычислить сумму знакопеременного ряда |х^(3n)|/(3n)!, где х-матрица ранга к (к и матрица задаются случайным образом)
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Операция умножения –поэлементная
'''
import numpy as np

N = int(input("Введите размерность квадратной матрицы больше 1 и меньше 31: "))
while (N < 1) or (N > 31) :
    N = int(input("Вы ввели неверное число\nВведите размерность квадратной матрицы больше 1 и меньше 31 : "))

A = np.random.randint(5, size=(N,N))
R = np.linalg.matrix_rank(A)
print("Матрица:\n", A)
print("Ранг матрицы:", R)

t = int(input('Введите количество знаков после запятой в результате вычисления: '))
t = 0.1**t

znam = 1
n = 1
summ = 0
delta = 0
drob = 1
while abs(drob) > t:
    delta += summ
    summ += (np.linalg.det(np.linalg.matrix_power(A, 3*n))) / znam
    n += 1
    znam = znam * (3*n) * (3*n - 1)
    drob = delta - summ
    delta = 0
    print(n - 1, ':', summ, ' ', drob)
print('Сумма знакопеременного ряда:', summ)
