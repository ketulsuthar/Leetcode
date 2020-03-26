'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''

#Solution-1 Using Loop

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        f = {}
        for i in nums:
            if i not in a:
                f[i] = f.get(i,0) + 1
             
                if f[i] > 1:
                    a[i] = f[i]
                    f.pop(i)
                  

        return f.popitem()[0]





#Solution-2 Using XOR

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in nums:
            t ^= i

        return t