import unittest

from src.fractions_math.add import Fraction, reduce


class Test(unittest.TestCase):
    def test_reduce_whole_number_to_itself(self):
        self.assertEquals(Fraction(1, 1), reduce(Fraction(1, 1)))
