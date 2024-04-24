from __future__ import annotations



class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    def simplify_fraction(self):
        divisor= Fraction.gcd(self.num, self.den)
        self.num //=  divisor
        self.den //= divisor

    def __add__(self, other: Fraction):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        result = Fraction(new_num, new_den)
        result.simplify_fraction()
        return result

    def __sub__(self, other: Fraction):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        result = Fraction(new_num, new_den)
        result.simplify_fraction()
        return result

    def __mul__(self, other: Fraction):
        new_num = self.num * other.den
        new_den = other.num * self.den
        result = Fraction(new_num, new_den)
        result.simplify_fraction()
        return result
    
    def __truediv__(self, other: Fraction):
        new_num = self.num * other.den
        new_den = self.den * other.num
        result = Fraction(new_num, new_den)
        result.simplify_fraction()
        return result
          
   

    def __str__(self):
        return f"{self.num}/{self.den}"

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a

