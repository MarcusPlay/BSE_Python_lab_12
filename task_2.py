#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Самостоятельно проработайте пример с оптимизацией хвостовых вызовов в Python.
# С помощью пакета timeit оцените скорость работы функций factorial и fib с использованием 
# интроспекции стека и без использования интроспекции стека. Приведите полученные результаты в отчет.

import sys
from functools import lru_cache
import timeit


sys.setrecursionlimit(10000)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

@lru_cache()
def factorial_tail_recursive(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail_recursive(n-1, n*acc)
    

if __name__=="__main__":
    x = int(input())

    time_recursive = timeit.timeit(str(factorial(x)), number=10000)
    time_tail_recursive = timeit.timeit(str(factorial_tail_recursive(x)), number=10000)

    print(f"Время выполнения обычной рекурсивной функции от {x}: {time_recursive}")
    print(f"Время выполнения оптимизированной хвостовой рекурсивной функции от {x}: {time_tail_recursive}")

