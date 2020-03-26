'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

'''



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f_str = ''
        if x < (2 ** 31)-1 and x >= (-2 ** 31):
            is_negative = 1
            if x < 0:
                is_negative = -1
                x= x * is_negative
            x = str(x)
            for c in x[-1::-1]:
                f_str += c
            num = int(f_str) * is_negative
            if num < (2 ** 31)-1 and num >= (-2 ** 31):
                return num
            return 0
        else:
            return 0







