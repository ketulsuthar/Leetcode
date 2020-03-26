'''
326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

'''

##Solution-1 Loop

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        elif n == 1: return True
        else:
            while n % 3 == 0:
                n//=3
            if n == 1: return True
            else: return False


##Solution-2 Recurrsion

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        elif n == 1: return True
        else:
            if n%3 == 0:
                return self.isPowerOfThree(n//3)
        return False
        