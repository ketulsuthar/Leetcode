'''
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
         
        triangle = [[1]]
        if numRows == 0: return []
        for i in range(2,numRows+1):
            tmp = [1]
            j=0
            while j <  len(triangle[-1])-1:
                tmp.append(triangle[-1][j]+triangle[-1][j+1])
                j+=1
            tmp.append(1)
            triangle.append(tmp)
        return triangle