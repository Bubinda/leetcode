# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def dfs(root):
            if root == None:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            ans[0] = max(ans[0] , 2 + left + right)

            return 1 + max(left , right)

        dfs(root)
        return ans[0]   
    

# more intuitive solution

# Idea 1 Implementation!
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
	    # Implement depth
        def depth(node: Optional[TreeNode]) -> int:
            return 1 + max(depth(node.left), depth(node.right)) if node else 0
        return depth(root.left) + depth(root.right)  # calculate diameter
    



# the solution above has the assumption that the largest diameter always takes the path through the root node
# the following code does not have this assumption

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0  # stores the maximum diameter calculated
            
    def depth(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum depth
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        # Calculate diameter
        curr_diameter = left + right
        if curr_diameter > self.max_diameter:
            self.max_diameter = curr_diameter
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left,right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        self.depth(root)  # root is guaranteed to be a TreeNode object
        return self.max_diameter