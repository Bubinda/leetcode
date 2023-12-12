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

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque([root])

        while q:
            right = None
            n = len(q)

            for i in range(n):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                result.append(right.val)
        return result
    


