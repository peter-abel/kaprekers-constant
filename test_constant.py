import unittest

from constant import generating_numbers, mylist, new_num,largest_number,count, subtract, small_number

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
        


class Test4(unittest.TestCase):
    def test_list_4(self):
        for i in range(1,10):
             subtract(i)
        
        self.assertGreaterEqual(count,1)

class Test5(unittest.TestCase):
    def test_list_5(self):
        subtract()
        self.assertEqual(new_num,6174)


if __name__ == "__main__":
    unittest.main()
