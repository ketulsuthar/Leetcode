'''
1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        first = root = TreeNode(preorder[0])
        
        for val in preorder[1:]:
            
            while first != None:
                
                if val < first.val:
                    if first.left == None:
                        first.left = TreeNode(val)
                        first = first.left
                    first = first.left
                else:
                    if first.right == None:
                        first.right = TreeNode(val)
                        first = first.right
                    first = first.right
                        
                        
            first = root
                
        return root
        
            