# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
# N = int(input('Введите день недели '))
# if (N == 6) or (N == 7):
#     print('Выходной день')
# else:
#     print('Будний день')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# X = int(input('Введите координату X '))
# Y = int(input('Введите координату Y '))
# Z = int(input('Введите координату Z '))
# for X in range(0,X+1):
#     for Y in range(0,Y+1):
#         for Z in range(0,Z+1):
#             print(not (X or Y or Z) == (not X and not Y and not Z))
#             print(X,Z,Y)
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# X = int(input('Введите координату X '))
# Y = int(input('Введите координату Y '))
# if (X < 0 and Y < 0):
#     print('Точка находится в 3 плоскости')
# elif (X < 0 and Y > 0):
#     print('Точка находится в 2 плоскости')
# elif (X > 0 and Y < 0):
#     print('Точка находится в 4 плоскости')
# elif (X > 0 and Y > 0):
#     print('Точка находится в 1 плоскости')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# N = int(input('Введите номер четверти '))
# if (N == 1):
#     print('диапазон x(0;∞),y(0;∞)')
# elif (N == 2):
#     print('диапазон x(-∞;0),y(0;∞)')
# elif (N == 3):
#     print('диапазон x(-∞;0),y(-∞;0)')
# elif (N == 4):
#     print(' диапазон x(0;∞),y(-∞;0)')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# A = str(input('Введите координаты точки A '))
# B = str(input('Введите координаты точки B '))
# x_A = (int(A.split(',')[0]))
# y_A = (int(A.split(',')[1]))
# x_B = (int(B.split(',')[0]))
# y_B = (int(B.split(',')[1]))
# from math import sqrt
# d = sqrt((x_B-x_A)**2+(y_B-y_A)**2)
# print(round(d,3))