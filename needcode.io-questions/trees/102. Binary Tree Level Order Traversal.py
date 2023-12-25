# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#iterative BFS

from colletions import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque([root])
        traversal = []
        while queue:
            level_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            traversal.append(level_list)
        return traversal
    


#recursive solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        count = 0

        def level(count , root):
            if root == None :
                return 

            if len(result) <= count:
                result.append([])    
            
            result[count].append(root.val)
            count += 1
            level(count , root.left)
            level(count , root.right) 

        level(count , root)
        return result
    



from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        values = []
        q = deque([root])

        while q: 

            length = len(q)
            inner = []

            for _ in range(length):

                node = q.popleft()
                inner.append(node.val)

                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)

            values.append(inner)

        return values
