# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if self.valid(row) == False:
                return False
        
        # Check columns
        for col in zip(*board):
            if self.valid(col) == False:
                return False
        
        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if self.valid(sub_box) == False:
                    return False
        
        return True

    def valid(self, unit):
        digits = set()
        for cell in unit:
            if cell != ".":
                if cell in digits:
                    return False
                digits.add(cell)
        return True
    





    

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r /3, c /3)
        for r in range(9):
            for c in range (9): 
                if board[r][c] == '.':
                    continue 
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]): 
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
    



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    if num in row[i] or num in col[j] or num in square[i//3 * 3 + j//3]:
                        return False
                    row[i].add(num)
                    col[j].add(num)
                    square[i//3 * 3 + j//3].add(num)
        return True
    


# in the following two solution all the elemnts that are not equal to "." are added into a list, if in the end the list and its set are of the same length the sudoku is valid
# this validation occurs from the fact that each element is saved alongside its row/coloumn or square and if in one of those three an alement is duplicated this would be filtered out by the set operation
# e.g. there would be two eghts in row 0 -> in the list there would be two elements like (0, '8') because there are two eghts in this row. 
# one of those would be filtered out by the set and then those two (list and the set) are not of the same length
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
    

# same as above but a little bit more concise
class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))