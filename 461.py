'''
461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        if (x >=0 and x <= (2**31)) and (y >=0 and y <= (2**31)):
            count = 0
            n = '{0:032b}'.format(x^y)
            l = len(n)-1
            i = 0
            while True:
                if i > l-i: break
                if n[i] == '1':
                    count += 1
                if n[l-i] == '1':
                    count +=1
                i += 1
            return count     
        else:
            return 0