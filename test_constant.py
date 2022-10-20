import unittest

from constant import generating_numbers, mylist, new_num,largest_number,count, subtract, small_number

'''Tests whether the length of the list has expected number'''
class TestConstant(unittest.TestCase):
    def test_list_int(self):
        generating_numbers()
        self.assertTrue(len(mylist), 8991)
        
'''Tests whether the integer is arranged in descending order'''
class Test2(unittest.TestCase):
    def test_list_2(self):
        y = 7325
        x = largest_number(5273)
        self.assertCountEqual(str(x),str(y))


'''Tests whether the integer is arranged in ascending order'''
class Test3(unittest.TestCase):
    def test_list_3(self):
        y = 3142
        x = small_number(1234)
        self.assertCountEqual(str(x),str(y))        
        


'''Tests that iterations are happening hence increase in count'''
class Test4(unittest.TestCase):
    def test_list_4(self):
        for i in range(1,10):
             subtract(i)
        
        self.assertGreaterEqual(count,1)


'''Tests whether the return value of the subtract function is 6174'''
class Test5(unittest.TestCase):
    def test_list_5(self):
       for i in range(20,25):
        subtract(i)
        self.assertEqual(new_num,6174)




class Test6(unittest.TestCase):
    def test_list_6(self):
         self.assertNotIn(3333,mylist)


         
if __name__ == "__main__":
    unittest.main()
