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
    numerator = fraction1.numerator + fraction2.numerator
    denominator = fraction1.denominator
    if numerator % denominator == 0:
        numerator = numerator/denominator
        denominator = 1
    return Fraction(numerator, denominator)
