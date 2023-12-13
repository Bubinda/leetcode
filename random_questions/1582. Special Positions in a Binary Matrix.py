# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:


# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:


# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m = len(mat)
        n = len(mat[0])
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    continue
                    
                good = True
                for r in range(m):
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                
                for c in range(n):
                    if c != col and mat[row][c] == 1:
                        good = False
                        break
                
                if good:
                    ans += 1
        
        return ans
    


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m = len(mat)
        n = len(mat[0])
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1 and sum(mat[row]) == 1 and sum(x[col] for x in mat) == 1:
                    ans += 1
        
        return ans




class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSum = [sum(row) for row in mat]
        colSum = [sum(row[j] for row in mat) for j in range(len(mat[0]))]
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    count += 1
        return count