'''
509. Fibonacci Number


The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.

'''

# Solution -1 [ Bottom-Up Approach using Memoization ]

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if  N <= 1: return N
        
        _f = {0:0,1:1}
        for i in range(2,N+1):
            _f[i] = _f[i-1]+_f[i-2]
        
        return _f[N]


# Solution -2 [ Recursion ]

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if  N <= 1: return N
        
        return self.fib(N-1) + self.fib(N-2)


# Solution -3 Using the golden ratio, a.k.a Binet's forumula: \varphi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887....

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)

