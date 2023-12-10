import unittest
import python2


class TestC(unittest.TestCase):
    def test_a(self):
        test = 5
        rs = python2.add(2, 3)
        self.assertEqual(test, rs)
if __name__ == '__main__':
    unittest.main()