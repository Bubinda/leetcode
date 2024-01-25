# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        queue = deque([root])

        while queue:
            right_most_node = None 
            length_queue = len(queue)

            for i in range(length_queue):
                curr_node = queue.popleft()
                if curr_node:
                    right_most_node = curr_node
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if right_most_node:
                solution.append(right_most_node.val)

        return solution
    


# other smart method to solve:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
         res = []

        def solve(root, lvl):
            if root:
        	    if len(res)==lvl:
        		    res.append(root.val)
                solve(root.right, lvl + 1)
                solve(root.left, lvl + 1)
            return 


        solve(root,0)
        return res