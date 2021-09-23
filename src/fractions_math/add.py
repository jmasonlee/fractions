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
    lcm = calculate_lcm(fraction1, fraction2, fraction1.denominator, fraction2.denominator)
    numerator = (fraction1.numerator * lcm) + fraction2.numerator
    denominator = fraction2.denominator

    if numerator % fraction2.denominator == 0:
        numerator = fraction1.numerator + fraction2.numerator
        numerator = numerator // fraction2.denominator
        denominator = 1

    fraction = Fraction(numerator, denominator)
    return fraction


def calculate_lcm(fraction1, fraction2, first_number, second_number):
    return second_number / first_number
