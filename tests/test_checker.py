from core.checker import Checker
import unittest

class CheckerTests(unittest.TestCase):

    def test_get_symbol_(self):
        checker_x = Checker(1)
        checker_o = Checker(2)
        self.assertEqual(checker_x.get_symbol(), 'x')
        self.assertEqual(checker_o.get_symbol(), 'o')