#!/usr/bin/env python3

import calc
import unittest



class CalcTest(unittest.TestCase):
    def setUp(self):
        self.obj = calc.Calc()

    def test_isNumeric_true(self):
        obj = calc.Calc()
        self.assertTrue(self.obj.isNumeric('0'))
        self.assertTrue(self.obj.isNumeric('1'))
        self.assertTrue(self.obj.isNumeric('2'))
        self.assertTrue(self.obj.isNumeric('3'))
        self.assertTrue(self.obj.isNumeric('4'))
        self.assertTrue(self.obj.isNumeric('5'))
        self.assertTrue(self.obj.isNumeric('6'))
        self.assertTrue(self.obj.isNumeric('7'))
        self.assertTrue(self.obj.isNumeric('8'))
        self.assertTrue(self.obj.isNumeric('9'))

    def test_isNumeric_False(self):
        self.assertFalse(self.obj.isNumeric(''))
        self.assertFalse(self.obj.isNumeric('a'))
        self.assertFalse(self.obj.isNumeric(' '))
        self.assertFalse(self.obj.isNumeric('あ'))
        self.assertFalse(self.obj.isNumeric('+'))
        self.assertFalse(self.obj.isNumeric('-'))
        self.assertFalse(self.obj.isNumeric('/'))
        self.assertFalse(self.obj.isNumeric('*'))
        self.assertFalse(self.obj.isNumeric('%'))
        self.assertFalse(self.obj.isNumeric('z'))

    def test_isOperator_true(self):
        self.assertTrue(self.obj.isOperator('+'))
        self.assertTrue(self.obj.isOperator('-'))
        self.assertTrue(self.obj.isOperator('*'))
        self.assertTrue(self.obj.isOperator('/'))

    def test_isOperator_False(self):
        self.assertFalse(self.obj.isOperator('@'))
        self.assertFalse(self.obj.isOperator('0'))
        self.assertFalse(self.obj.isOperator('3'))
        self.assertFalse(self.obj.isOperator('6'))
        self.assertFalse(self.obj.isOperator('9'))
        self.assertFalse(self.obj.isOperator('z'))
        self.assertFalse(self.obj.isOperator('++'))
        self.assertFalse(self.obj.isOperator('--'))
        self.assertFalse(self.obj.isOperator('=='))
        self.assertFalse(self.obj.isOperator('**'))
        self.assertFalse(self.obj.isOperator('//'))



if __name__ == '__main__':
    unittest.main()
