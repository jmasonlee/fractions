import unittest

from src.fractions_math.add import Fraction, reduce


class Test(unittest.TestCase):
    def test_reduce_one_to_one(self):
        self.assertEquals(Fraction(1), reduce(Fraction(1)))

    def test_reduce_whole_number_to_itself(self):
        self.assertEquals(Fraction(2), reduce(Fraction(2)))

    def test_numerator_is_multiple_of_denominator(self):
        self.assertEquals(Fraction(3), reduce(Fraction(6, 2)))

    def test_fraction_reduces_to_itself(self):
        self.assertEquals(Fraction(1, 5), reduce(Fraction(1, 5)))

    def test_denominator_is_multiple_of_numerator(self):
        self.assertEquals(Fraction(1, 3), reduce(Fraction(5, 15)))

    def test_numerator_and_denominator_share_a_factor(self):
        self.assertEquals(Fraction(7, 9), reduce(Fraction(21, 27)))


