# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]






# works but runs very slowly
# O(n^2) time | O(n) space
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        # Iterate through rows and columns
        for i in range(n):
            for j in range(n):
                row = grid[i]
                col = [grid[k][j] for k in range(n)]

                # Check if the row and column are equal
                if row == col:
                    count += 1

        return count


#does also work but runs way faster then the previous one
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        row_dict = {}

        # Create a dictionary of rows as strings and their counts
        for i in range(n):
            row_str = str(grid[i])
            if row_str in row_dict:
                row_dict[row_str] += 1
            else:
                row_dict[row_str] = 1

        # Iterate through columns and check if they are equal to rows
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            col_str = str(col)

            if col_str in row_dict:
                count += row_dict[col_str]

        return count