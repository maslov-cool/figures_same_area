from turtle import *
from random import *
from math import *


def shape(s, x, y):
    n = randint(3, 7)
    a = sqrt((s * 4 * tan(radians(180) / n)) / n)
    corner = 360 / n

    # перемещаем
    penup()
    goto(x - ((sqrt((s * 4 * tan(radians(60))) / 3) - sqrt((s * 4 * tan(radians(180) / n)) / n)) / 2), y)
    pendown()

    fillcolor(randint(0, 256), randint(0, 256), randint(0, 256))
    begin_fill()
    left(180)
    for _ in range(n):
        forward(a)
        left(corner)
    setheading(0)
    end_fill()


def shapes(s):
    hideturtle()
    length = sqrt((s * 4 * tan(radians(60))) / 3)
    distance = length / 4
    x, y = 0, 0
    while True:
        answer = input('Сразу вывести результат? Введите да / нет ').strip().lower()
        if answer == 'да':
            Screen().tracer(0, 0)
            for _ in range(5):
                for _ in range(5):
                    shape(s, x, y)
                    y -= (length + distance)
                y = 0
                x += length + distance
            Screen().update()
            break
        elif answer == 'нет':
            for _ in range(5):
                for _ in range(5):
                    shape(s, x, y)
                    y -= (length + distance)
                y = 0
                x += length + distance
            break
        else:
            print('Я вас не понял')
            continue


shapes(int(input()))