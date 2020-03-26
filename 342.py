'''
342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''

#Solution-1 Recursion

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n <= 0: return False
        elif n == 1: return True
        else:
            if n%4 == 0:
                return self.isPowerOfFour(n//4)
        return False
        

#Solution-1 Loop