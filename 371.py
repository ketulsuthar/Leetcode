'''
371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

'''

class Solution(object):
    def getSum(self, x, y):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([x,y])