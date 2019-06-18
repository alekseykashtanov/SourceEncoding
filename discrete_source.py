"""
    @file Файл с описанием класса дискр. источника
    @note Источник должен быть стационарным, без памяти
"""

import json
from fractions import Fraction
from math import log


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

    def gen_encoding(self, R, eps):
        if len(self.probabilities) != 2:
            print("Не мучайте меня, дайте два!!")
            return None

