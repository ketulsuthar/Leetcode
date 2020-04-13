'''
476. Number Complement
Easy

685

76

Add to List

Share
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

'''


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 1: return 0
        elif num == 0: return 1
        else:
            _num = []
            total =0
            while True:
                rem = num%2
                num = num//2
                _num.append(rem)
                total = (total*10)+1
                if num == 1:
                    _num.append(num)
                    total = (total*10)+1
                    break
            
            return int(str(total - int(''.join([ str(i) for i in _num[::-1]]))),2)
        