# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
dayweek= int(input('Введите день недели(от 1 до 7): ')) # где 1 условно это начало недели

if dayweek == 6 or dayweek == 7:
    print("выходной")
else:
    print("не выходной")

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите значение координаты x:  '))
y = int(input('Введите значение координаты y:  '))
if x > 0 and y > 0:
    print('Точка находится в I')
elif x < 0 and y > 0:
    print('Точка находится в II')
elif x < 0 and y < 0:
    print('Точка находится в III')
elif x > 0 and y < 0:
    print('Точка находится в IV четверти')
elif x == 0 and y != 0:
    print('Точка находится на оси y')
elif x != 0 and y == 0:
    print('Точка находится на оси x')
else:
    print('X ≠ 0 и Y ≠ 0')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input('Введите номер четверти от 1 до 4: '))
if quarter == 1:
    print('I - диапазон возможных координат  x > 0  y > 0')
elif quarter == 2:
    print('II - диапазон возможных координат  x < 0  y > 0')
elif quarter == 3:
    print('III - диапазон возможных координат  x < 0  y < 0')
elif quarter == 4:
    print('IV - диапазон возможных координат  x > 0  y < 0')
else:
    print('не верный диапозон')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Xa = int(input('Введите X координату первой точки: '))
Ya = int(input('Введите Y координату первой точки: '))
Xb = int(input('Введите X координату второй точки: '))
Yb = int(input('Введите Y координату второй точки: '))
Ac = Yb-Ya
Bc = Xb-Xa
print(round((Ac ** 2 + Bc ** 2) ** 0.5, 4))