'''
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Solution -1 Iterative

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        
        _inorder = []
        stack = []
        curr = root
        while curr != None or len(stack) > 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            _inorder.append(curr.val)
            curr = curr.right
        return _inorder

# Solution-2 Recurrsive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        _inorder = []
        def inorder(root):
            if root == None: return
            inorder(root.left)
            _inorder.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return _inorder


# Solution - 3 Threaded Binary Approach


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        _inorder = []
        curr = root
        while curr != None:
            
            if curr.left == None:
                _inorder.append(curr.val)
                curr= curr.right
            else:
                prev = curr.left
                while prev.right !=  None:
                    prev=prev.right
                    
                prev.right = curr
                tmp = curr
                curr= curr.left
                tmp.left = None
               
        return _inorder
                
            
