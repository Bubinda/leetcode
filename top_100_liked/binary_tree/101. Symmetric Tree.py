# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symetric(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            
            return symetric(r1.left, r2.right) and symetric(r1.right, r2.left)

        return symetric(root,root)
    

# without recursion but with a stack

class Solution:
    def isSymmetric(self, root):
        stack = []
        if root: stack.append([root.left, root.right])

        while(len(stack) > 0):
            left, right = stack.pop()
            
            if left and right:
                if left.val != right.val: return False
                stack.append([left.left, right.right])
                stack.append([right.left, left.right])
        
            elif left or right: return False
        
        return True