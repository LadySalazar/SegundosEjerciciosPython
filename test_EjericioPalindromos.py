import unittest

from EjericioPalindromos import saberPalindromo


class Test(unittest.TestCase):
    def test_EjercicioPalindromo(self):
        self.assertEqual(True, saberPalindromo("sometemos"))


if __name__ == '__main__':
    unittest.main()

