# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Inorder traversal assumes the following traversal order: left node -> node -> right node

# There are two ways to do the traversal: recursive and iterative. I'll do both

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def inorderIterative(self, root: TreeNode) -> List[int]:
        
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def inorderRecursive(self, root: TreeNode) -> List[int]:
        res = []
        
        def inorder(node):
            if node == None:
                return
            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)
            return 
        inorder(root)
        return res