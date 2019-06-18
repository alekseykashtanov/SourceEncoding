"""
    @file Файл с описанием класса дискр. источника
    @note Источник должен быть стационарным, без памяти
"""

import json
from fractions import Fraction
from math import log, log2, fabs
from sympy import Symbol, solve, log2


def log_solver(R, p):
	x = Symbol('x')
	return solve(-(p + x) * log2(p + x) - (1 - p - x) * log2(1 - p - x) - R)


def local_entropy(p):
	return - (p * log2(p) + (1 - p) * log2(1 - p))


def check_correctness(desc):
    sum_ = 0
    for i in desc.values():
        sum_ += float(Fraction(i))
    if sum_ != 1:
        raise KeyError


class DiscreteSource:
    # src : dict - Description of DS

    def __init__(self, desc):
        self.src = json.load(desc)
        check_correctness(self.src)
        self.probabilities = self.src.values()

    def entropy(self):
        return_ = 0
        capacity = len(self.probabilities)
        for i in self.probabilities:
            if i:   # Дополнение в нуле по непрерывности
                return_ -= i * log(i, capacity)
        return return_

    def gen_encoding(self, R, eps, q, out_file):
    	# Проверка условий
        if len(self.probabilities) != 2:
            print("Не мучайте меня, дайте два!!")
            return None
        # Насильное изменение вероятностей
        # Ну хочется, чтоб по теории
        if self.src["1"] > 0.5:
        	self.src["1"], self.src["0"] = self.src["0"], self.src["1"]
        p = src["1"]
        if R <= entropy():
        	print("Невозможно сгенерировать код для такой скорости")
        	return None

        # Определение нужного индекса n для последовательности T_n
        local_eps = log_solver(R, p)
        n = 1
        expr_ = p * (1 - p) / n * local_eps
        while (expr_ < eps):
        	n += 1
        	expr_ = p * (1 - p) / n * local_eps

        # Вычисление мощности множества T_n
        capacity = 0
        for i in range(2 ** n):
        	k = bin(i).count('1')
        	if fabs(k - n * p) < n * local_eps:
        		capacity += 1

        # Определение длины кодового слова
       	m = 1
       	while (q ** m < capacity):
       		m += 1

        return m
