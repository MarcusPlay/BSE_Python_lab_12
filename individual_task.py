#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_min_recursive(X, n):
    if n == len(X) - 1:
        return X[n]
    
    rest_min = find_min_recursive(X, n + 1)
    
    if X[n] < rest_min:
        return X[n]
    else:
        return rest_min

if __name__=="__main__":
    X = list(map(float, input("Введите значения списка через пробел:\n").split()))
    n = int(input("Введите индекс с которого будет вестись поиск: "))
    result = find_min_recursive(X, n)
    print(f"Минимальный элемент списка, начиная с {n}-го: {result}")

