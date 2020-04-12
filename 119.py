'''
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = [1]
        if rowIndex == 0: return triangle
        for i in range(1,rowIndex+1):
            tmp = [1]
            j=0
            while j <  len(triangle)-1:
                tmp.append(triangle[j]+triangle[j+1])
                j+=1
            tmp.append(1)
            triangle = tmp
        return triangle