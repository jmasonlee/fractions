import math


class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


def add(fraction1: Fraction, fraction2: Fraction) -> Fraction:
    factor1 = calculate_factor(fraction1.denominator, fraction2.denominator)
    numerator = (fraction1.numerator * factor1) + fraction2.numerator
    denominator = fraction2.denominator

    fraction = Fraction(numerator, denominator)
    fraction = reduce(fraction)
    return fraction


def reduce(fraction):
    denominator = fraction.denominator
    numerator = fraction.numerator
    gcd = math.gcd(int(numerator), int(denominator))
    numerator = numerator // gcd
    denominator = denominator // gcd
    fraction = Fraction(numerator, denominator)
    return fraction


def calculate_factor(first_number, second_number) -> int:
    return second_number / first_number
