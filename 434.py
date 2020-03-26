'''
434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

'''

# Solution -1

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == '': return 0
        s = s.split(" ")
        first = 0
        last = len(s)- 1
        count=0
        while first <= last:
            if s[first] and s[last] and first != last:
                count+=2
            elif s[first] or s[last]:
                count+=1
            first+=1
            last-=1
        return count



# Solution -2

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for c in s.split(" "):
            if c:
                count+=1
        return count