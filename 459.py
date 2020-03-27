'''
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

# Solution -1

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        found = False
        sub = ''
        l = len(s)
        for i in range(l):
            sub+=s[i]
            for j in range(i+1,l,len(sub)):
                if sub ==  s[j:len(sub)+j]:
                    found = True
                else:
                    found = False
                    break
            if found:
                return True
        return False



# Solution -2

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in s[1:]+s[:-1]
        