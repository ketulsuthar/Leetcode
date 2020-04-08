'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''

# Solution-1

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        s=s.lower()
        while i<=j:
            if s[i].isalnum() and s[j].isalnum() :
                if s[i] != s[j]:
                    return False
                else:
                    i+=1
                    j-=1
            elif s[i].isalnum():
                j-=1
            else:
                i+=1
        return True


# Solution-2


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        palim = list(filter(lambda c : c.isalnum(),s.lower()))
        
        return palim == palim[::-1]
  