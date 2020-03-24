'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) >=1:
            prefix=strs[0]
            for s in strs[1:]:
                ph=''
                for i,j in zip(prefix,s):
                    if i==j:
                        ph+=i
                    else:
                        break
                if ph:
                    prefix=ph
                else:
                    return ''
            return prefix
                       
        else:
            return ""