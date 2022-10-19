import unittest

from constant import generating_numbers, mylist, largest_number, small_number

class TestConstant(unittest.TestCase):
    def test_list_int(self):
        generating_numbers()
        self.assertTrue(len(mylist), 8991)
        

class Test2(unittest.TestCase):
    def test_list_2(self):
        y = 7325
        x = largest_number(5273)
        self.assertCountEqual(str(x),str(y))

class Test3(unittest.TestCase):
    def test_list_3(self):
        y = 3142
        x = small_number(1234)
        self.assertCountEqual(str(x),str(y))        
        



if __name__ == "__main__":
    unittest.main()
