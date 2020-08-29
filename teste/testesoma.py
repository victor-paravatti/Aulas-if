import unittest
from Python.aula_1 import soma


class TesteSoma(unittest.TestCase):
    def test_retorno_soma(self):
        self.assertEqual(soma(10, 10), 20)
