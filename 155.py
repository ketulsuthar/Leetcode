'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.i = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.i == None:
            self.i= 0
        else:
             self.i+=1
        _min = x  
        
        if len(self.stack) > 0 and self.stack[-1]['min'] <  _min:
            _min = self.stack[-1]['min']       
            
        self.stack.append({'n':x,'min':_min})
                     
        
    def pop(self):
        """
        :rtype: None
        """
        if self.i >= 0:
            self.stack = self.stack[0:self.i]
            self.i-=1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.i]['n']

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.i]['min']


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()