# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def dfs(i):
            if i == len(nums)-1:
                sol.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return sol
    


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        return result
    


# for me this one is the most intuitive
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        solution = []

        def backtrack():
            if len(nums) == len(solution):
                perms.append(solution[:])
                return

            for num in nums:
                if not num in solution:
                    solution.append(num)
                    backtrack()
                    solution.pop()

        backtrack()
        return perms