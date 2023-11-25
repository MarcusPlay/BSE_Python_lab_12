#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Самостоятельно изучите работу со стандартным пакетом Python timeit. 
# Оцените с помощью этого модуля скорость работы итеративной и рекурсивной версий функций factorial и fib. 
# Во сколько раз измениться скорость работы рекурсивных версий функций factorial и fib при использовании декоратора lru_cache? 
# Приведите в отчет и обоснуйте полученные результаты.

import timeit
from functools import lru_cache
import sys

sys.set_int_max_str_digits(0)
sys.setrecursionlimit(10000)

# Итеративная версия факториала
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Рекурсивная версия факториала
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Итеративная версия чисел Фибоначчи
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Рекурсивная версия чисел Фибоначчи
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Декоратор lru_cache для рекурсивных функций
@lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive_cached(n - 1)

@lru_cache(maxsize=None)
def fib_recursive_cached(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)
    

def main(x, y):
    print(f"\nfactorial_iterative({x}) --------> {timeit.timeit(str(factorial_iterative(x)), number=10000)}")
    print(f"factorial_recursive({x}) --------> {timeit.timeit(str(factorial_recursive(x)), number=10000)}")
    print(f"factorial_recursive_cached({x}) -> {timeit.timeit(str(factorial_recursive_cached(x)), number=10000)}")
    print(f"\nfib_iterative({y}) ----------------> {timeit.timeit(str(fib_iterative(y)), number=10000)}")
    print(f"fib_recursive({y}) ----------------> {timeit.timeit(str(fib_recursive(y)), number=10000)}")
    print(f"fib_recursive_cached({y}) ---------> {timeit.timeit(str(fib_recursive_cached(y)), number=10000)}\n")
    
if __name__=="__main__":
    x = int(input())
    y = int(input())
    main(x, y)