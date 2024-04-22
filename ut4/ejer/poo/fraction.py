from __future__ import annotations



class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def __add__(self, other: Fraction):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other: Fraction):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other: Fraction):
        new_num = self.num * other.den
        new_den = other.num * self.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other: Fraction):
        new_num = self.num / other.den
        new_den = other.num / self.den
        return Fraction(new_num, new_den)

    def __str__(self): ...

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
