from django.test import TestCase    
from app.calc import add, sub


class CalcTest(TestCase):
    def test_add_number(self):
        """test to add two numbers"""
        self.assertEqual(add(3,5),8)
    
    def test_sub_tdd(self):
        """
        running test using test driven devlopment (tdd)
        """
        self.assertEqual(sub(23,5),18)