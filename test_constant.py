import unittest

from constant import generating_numbers, mylist

class TestConstant(unittest.TestCase):
    def test_list_int(self):
        generating_numbers()
        self.assertTrue(len(mylist), 8991)
        



if __name__ == "__main__":
    unittest.main()
