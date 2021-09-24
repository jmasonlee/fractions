import math


class Fraction:
    def __init__(self, numerator, denominator=1):
        reduced_numerator, reduced_denominator = reduce_numerator_and_denominator(numerator, denominator)
        self.numerator = reduced_numerator
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
    og_denominator = fraction.denominator
    og_numerator = fraction.numerator
    new_denominator, new_numerator = reduce_numerator_and_denominator(og_numerator, og_denominator)
    fraction = Fraction(new_numerator, new_denominator)
    return fraction


def reduce_numerator_and_denominator(og_numerator, og_denominator):
    gcd = math.gcd(int(og_numerator), int(og_denominator))
    new_numerator = og_numerator // gcd
    new_denominator = og_denominator // gcd
    return new_denominator, new_numerator


def calculate_factor(first_number, second_number) -> int:
    return second_number / first_number
