import unittest
from calculadora import soma
# testando pipeline
class TestSomar(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)
        
    def test_soma_negativos(self):    
        self.assertEqual(soma(-1, 1), 0)
        
    def test_soma_com_zero(self):
        self.assertEqual(soma(5, 0), 5) # Esse teste falha
        
if __name__ == '__main__':
    unittest.main()