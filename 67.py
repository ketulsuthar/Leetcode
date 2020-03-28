'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

# Solution -1

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        no=0
        for i,v1 in enumerate(a[::-1]):
            no+= (2**i * int(v1))

        for i,v2 in enumerate(b[::-1]):
            no+= (2**i * int(v2))
        return '{0:0b}'.format(no)



# Solution -2

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{0:0b}'.format(int(a,2)+int(b,2))