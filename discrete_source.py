"""
    @file Файл с описанием класса дискр. источника
    @note Источник должен быть стационарным, без памяти
"""

import json
from fractions import Fraction
from math import log2


def gen_code(q, size):
    result = []
    code_len = 1
    while q ** code_len < size:
        code_len += 1
    for i in range(size):
        vec = ""
        elem = i
        for j in range(code_len):
            vec = str(elem % q) + vec
            elem //= q
        result.append(vec)
    return result


def print_encoding(hps, n, q):
    code = gen_code(q, len(hps))
    print(code)
    print("Кодирование: ")
    print("{:<10}\t{}".format("<HPS_ELEM>", "<ENCODING_WORD>"))
    for i in range(len(hps)):
        print("{:<10}\t{:<10}".format(hps[i], code[i]))



def check_correctness(desc):
    sum_ = 0
    for i in desc.values():
        sum_ += float(Fraction(i))
    if sum_ != 1:
        raise KeyError


class DiscreteSource:
    # src : dict    - Описание источника
    # ent : float   - энтропия источника

    def __init__(self, desc):
        self.src = json.load(desc)
        check_correctness(self.src)
        for key in self.src:
            self.src[key] = float(Fraction(self.src[key]))
        self.probabilities = self.src.values()
        self.ent = self.entropy()

    def entropy(self):
        return_ = 0
        for i in self.probabilities:
            if i:   # Дополнение в нуле по непрерывности
                return_ -= i * log2(i)
        return return_

    def calc_prob(self, hps):
        p = 0
        for elem in hps:
            cur_p = 1
            for bit in bin(elem)[2:]:
                cur_p *= self.src[bit]
            p += cur_p
        return p

    # HPS - высоковероятное множество
    def generate_hps(self, eps, n):
        result = []
        left_b = self.ent - eps
        right_b = self.ent + eps
        for elem in range(2 ** n):
            ones = bin(elem).count('1')
            p = self.src["1"] ** ones * self.src["0"] ** (n - ones)
            if left_b <= -log2(p) / n <= right_b:
                result.append(elem)
        print(result)
        return result

    def gen_encoding(self, R, eps, q):
        n = 1
        while True:
            print('n = ', n)
            hps_n = self.generate_hps(eps, n)
            if self.calc_prob(hps_n) >=  1 - (R - self.ent):
                break
            n += 1
        print_encoding(hps_n, n, q)
