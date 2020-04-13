'''
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


'''

# Solution -1 Boyer-Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        count = 0
        _num = None
        
        for n in nums:
            if count == 0:
                _num = n
            
            count += 1 if n == _num else -1
        
        return _num


# Solution -2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        return nums[len(nums)//2]



# Solution -3

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        count = 0
        _num = None
        i = 0
        j = len(nums)-1
        
        while i <= j:
            if count == 0:
                _num = nums[i]
            
            count += 1 if nums[i] == _num else -1
            count += 1 if nums[j] == _num else -1
            i+=1
            j-=1
        
        return _num