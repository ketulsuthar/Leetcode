'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Ref.

Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
Initially, let p equal 2, the first prime number.
Starting from p2, count up in increments of p and mark each of these numbers greater than or equal to p2 itself in the list. These numbers will be p(p+1), p(p+2), p(p+3), etc..
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.

https://www.geeksforgeeks.org/sieve-of-eratosthenes/

'''
#  Eratosthenes’ method

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        _prime = [True]*n
        _count = 0
        for i in range(2,n):
            if _prime[i] == True:
                _count+=1
                for j in range(i*i,n,i):
                    _prime[j] = False        
        
        return _count
                