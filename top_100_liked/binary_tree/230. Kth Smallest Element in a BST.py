# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we need a stack and a counter var to kkep track of the already visited nodes
        element_counter = 0
        stack = []
        curr_node = root

        # then we ran the loop as long as we have elments in the stack of if we do not have ran over the whole tree
        while curr_node or stack:
            # first we go as far to the left in the tree as possible and append all nodes on the track to the stack
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left

            # then we pop the last node -> the lowest node with the lowest value
            curr_node = stack.pop()
            # and increase the element counter
            element_counter +=1

            # if the element counter reaches the k-th element we return the value of this element
            if element_counter == k:
                return curr_node.val
            # otherwise we go to the right node of our current node 
            else:
                curr_node = curr_node.right


# unsing an extra array to store all the smallest elements from the left subtrees in increasing oder (inorder traversal of the tree)
# then accessing the array with the k-1 index to get the k-th element
# this solution is also recursive

class Solution(object):
    def kthSmallest(self, root, k):
        values = []
        self.inorder(root, values)
        return values[k - 1]

    def inorder(self, root, values):
        if root is None:
            return
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)



# the pure recursive approach is very similiar to the first approach using a stack
class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0
        self.inorderTraversal(root, k)
        return self.result
    
    def inorderTraversal(self, node, k):
        if not node or self.count >= k:
            return
        
        self.inorderTraversal(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        
        self.inorderTraversal(node.right, k)