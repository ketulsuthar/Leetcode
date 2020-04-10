'''
844.  Backspace String Compare


Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''


# Solution -1


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i=j=0
        s=''
        t=''
        while i < len(S) or j < len(T):
            if i < len(S):
                if S[i] == '#':
                    s = s[:-1]
                else:
                    s+=S[i]
            i+=1
                  
            if j < len(T): 
                if T[j] == '#':
                    t=t[:-1]
                else:
                    t+=T[j]
            j+=1
        return s==t

# Solution -2


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s=''
        t=''
        for c in S:
            if c != '#':
                s+=c
            else:
                s=s[:-1]
        for c in T:
            if c != '#':
                t+=c
            else:
                t=t[:-1]
        return s==t


