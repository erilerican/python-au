#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #добавление математического модуля
import numpy #добавление математического модуля для работы с массивами
import matplotlib.pyplot as mpp #что-то, без чего не работает


if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]#создание списка аргументов функции через массив
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    ) #задание уравнения функции
    mpp.show() #вывод графика на экран
