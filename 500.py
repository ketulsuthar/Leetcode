'''
500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {'a': '2', 'b': '3', 'c': '3', 'd': '2', 'e': '1', 'f': '2', 'g': '2', 'h': '2', 'i': '1', 'j': '2', 'k': '2', 'l': '2', 'm': '3', 'n': '3', 'o': '1', 'p': '1', 'q': '1', 'r': '1', 's': '2', 't': '1', 'u': '1', 'v': '3', 'w': '1', 'x': '3', 'y': '1', 'z': '3'}
        
        _words =[]
        for word in words:
            i = 0
            count=1
            line = keyboard.get(word[i].lower())
            while i < len(word)-1:
                if line != keyboard.get(word[i+1].lower()):
                    break
                else:
                    count+=1
                i+=1
            if count == len(word):
                _words.append(word)
                    
        return _words
            