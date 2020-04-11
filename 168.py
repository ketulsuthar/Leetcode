'''
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        _S=''
        while n//26 != 0:
            r = 26 if n%26 == 0 else n%26
            _S+=chr(r+64)
            
            if r == 26:n-=26
                
            n = n//26 
        if n > 0:
             _S+=chr(n+64)
        return _S[::-1]
                
            