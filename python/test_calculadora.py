import unittest

def multiplicar(a, b):
    return a * b

class TestCalculadora(unittest.TestCase):
    def test_multiplicacion(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(0, 10), 1)
        self.assertEqual(multiplicar(-2, 4), -8)

if __name__ == '__main__':
    unittest.main()
