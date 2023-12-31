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
    

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = [0]

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)
            maxx[0] = max(maxx[0], left+right)

            return 1 + max(left, right)

        dfs(root)
        return maxx[0]