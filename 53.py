'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        previous = nums[0]
        i = 1
        while i < len(nums):
            sum_t = previous + nums[i]
            max_sum = max(sum_t,max_sum,nums[i])
            previous = max(sum_t,nums[i])
            i+=1
        return max_sum