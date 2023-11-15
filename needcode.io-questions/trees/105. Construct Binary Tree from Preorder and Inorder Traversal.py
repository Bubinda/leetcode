# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # because of the properties of the two lists we can derive the following:
        # the preorder does alsoways start with the root node of our current tree -> first is root ,second is root of left tree , and so on 
        # the inoder does alsways contain the root and all elements to the left of the root are the elements of the leaft subtree and all to the right are all elements of the right subtree
        # if then the length of the left and right subtrees of the current root are taken from the inoder and with those the preorder lists are split then we can derive all elemnts of the subtrees 
        # so in the recursive solution only the splits need to be returned to the next recursion level
        root = TreeNode(preorder[0])
        mid = inorder.index(root) # the index of the root node in the inorder list, so we get all the elements of the left anf right subtrees
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) # give the left subtree all elemtns to the left side of the inorder and the rest of the preorder list without the current root
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])# gev the right tree the same as the left tree but shifted
        return root 
