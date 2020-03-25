'''
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_str = [c for c in s]
        head =  0
        tail = len(s)-1
        vowels ='aeiouAEOUI'
        while head < tail:
            if s_str[head] not in vowels:
                head+=1
            elif s_str[tail] not in vowels:
                tail-=1
            else:
                s_str[head], s_str[tail] = s_str[tail], s_str[head]
                tail-=1
                head+=1
        return ''.join(s_str)
            
        