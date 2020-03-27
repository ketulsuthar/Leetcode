'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

# Solution -1


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        is_balance = True
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if len(stack) > 0:
                  removed_ch = stack.pop()
                  #print(removed_ch)
                  
                  #print(ch)
                  if (removed_ch == "(" and ch == ")") or (removed_ch == "{" and ch == "}") or (removed_ch == "[" and ch == "]"):
                      continue
                  else:
                    is_balance = False
                    break
                else:
                    is_balance = False
                    break
        if len(stack) > 0 :
            is_balance = False
        return is_balance
                
# Solution- 2

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        mapping_ch = {")": "(", "}": "{", "]": "["}
     
        for ch in s:
            if ch in mapping_ch:
                removed_ch = stack.pop() if stack else "9"
                if mapping_ch[ch] != removed_ch:
                    return False
            else:
                stack.append(ch)
                
        return not stack
                