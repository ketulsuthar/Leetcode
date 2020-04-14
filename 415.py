'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

# Solution -1

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def _sum(num):
        
            value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
            _num = 0
            for i in num:
                _num = _num*10 + value[i]
            
            return _num
        return str(_sum(num1) + _sum(num2))   


# Solution -2
# 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        no = 0
        for i,_n in enumerate(num1[::-1]):
            _n = ord(_n)-48
            no+= (_n * (10**i))
            
        for i,_n in enumerate(num2[::-1]):
            _n = ord(_n)-48
            no+= (_n * (10**i))
            
        return str(no)            
                