import calc
import unittest
class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(20,20),40)
    def test_sub(self):
        self.assertEqual(calc.sub(10,5),5)
    def test_multi(self):
        self.assertEqual(calc.multi(10,5),40)
    def test_div(self):
        self.assertEqual(calc.div(10,2),5)

if __name__ == "__main__":
     unittest.main(verbosity=2)

