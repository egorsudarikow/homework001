# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти:'))

if a == 1:
    print('В первой четверти X > 0 ; y > 0')
elif a == 2:
    print('В Второй четверти x < 0 ; y > 0')
elif a == 3:
    print('В третьей четверти x < 0 ; y < 0')
elif a == 4:
    print('В четвертой четверти x > 0 ; y 0')
