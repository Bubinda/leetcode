# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false


#recursive DFS:
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return ((self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)))
    


#iterative DFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!= q.val:
            return False
        
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val!= q.val:
                return False
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True


#iterative BFS
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!= q.val:
            return False
        
        queue = [(p, q)]
        while queue:
            p, q = queue.pop(0)
            if not p and not q:
                continue
            if not p or not q or p.val!= q.val:
                return False
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True
    



class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not q or not p: return False
        if p.val != q.val: return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    

