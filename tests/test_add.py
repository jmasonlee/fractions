import unittest
from unittest import TestCase

from src.fractions_math import add
from src.fractions_math.add import Fraction


class Test(TestCase):

    def test_add_zeroes(self):
        self.assertEqual(Fraction(0), add.add(Fraction(0), Fraction(0)))

    def test_add_right_zero(self):
        self.assertEqual(Fraction(1), add.add(Fraction(1), Fraction(0)))

    def test_add_left_zero(self):
        self.assertEqual(Fraction(2), add.add(Fraction(0), Fraction(2)))

    def test_add_right_negative(self):
        self.assertEqual(Fraction(2), add.add(Fraction(4), Fraction(-2)))

    def test_add_left_negative(self):
        self.assertEqual(Fraction(1), add.add(Fraction(-3), Fraction(4)))

    def test_add_negatives(self):
        self.assertEqual(Fraction(-5), add.add(Fraction(-3), Fraction(-2)))

    def test_result_is_a_fraction_when_inputs_do_not_make_a_whole(self):
        self.assertEqual(Fraction(7, 9), add.add(Fraction(4, 9), Fraction(3, 9)))

    def test_two_numbers_make_a_whole(self):
        self.assertEqual(Fraction(1), add.add(Fraction(1, 3), Fraction(2, 3)))

    @unittest.skip
    def test_one_denominator_is_a_multiple_of_the_other(self):
        self.assertEqual(Fraction(3, 4), add.add(Fraction(1, 2), Fraction(1, 4)))
