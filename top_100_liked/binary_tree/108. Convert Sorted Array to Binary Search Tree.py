# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        if not n:
            return None
        
        mid = (n-1)//2
        root = TreeNode(nums[mid])

        root.left = (self.sortedArrayToBST(nums[:mid]))
        root.right = (self.sortedArrayToBST(nums[mid+1:]))
        
        return root
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length_array = len(nums)

        if not length_array:
            return None

        root_node = length_array//2
        root = TreeNode(nums[root_node])

        root.left = self.sortedArrayToBST(nums[:root_node])
        root.right = self.sortedArrayToBST(nums[root_node+1:])

        return root
    


# other way to solve it recusrively

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)
    def sortedArrayToBSTHelper(self, nums, floor, ceiling):
        if floor > ceiling: return None
        middleIndex = (floor + ceiling) // 2
        n = TreeNode(nums[middleIndex])
        n.left = self.sortedArrayToBSTHelper(nums, floor, middleIndex - 1)
        n.right = self.sortedArrayToBSTHelper(nums, middleIndex + 1, ceiling)
        return n
    


# a iterative solution but this one is not as simple as the recursive one in my opinion

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        # Each item in the stack holds: floor, ceiling, parent and parent's direction.
        stack = [(0, len(nums) - 1, None, None)]
        root = None
        while stack:
            floor, ceiling, parent, direction = stack.pop()
            middleIndex = (floor + ceiling) // 2
            n = TreeNode(nums[middleIndex])
            
            # Add the root node. parent should only ever be null in this one case.
            if not parent:
                root = n
            else:
                if direction == 'l':
                    parent.left = n
                elif direction == 'r':
                    parent.right = n
            
            # Add the next items to the stack, as necessary. Add right first.
			# Similar to the recursive approach, both floor and ceiling should never cross.
            if middleIndex + 1 <= ceiling:
                stack.append((middleIndex + 1, ceiling, n, 'r'))
            if floor <= middleIndex - 1:
                stack.append((floor, middleIndex - 1, n, 'l'))
        return root