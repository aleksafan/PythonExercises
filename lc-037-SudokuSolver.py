# https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# 
# Example 1:
# 
# Input: board = [["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],
# ["6","7","2","1","9","5","3","4","8"],
# ["1","9","8","3","4","2","5","6","7"],
# ["8","5","9","7","6","1","4","2","3"],
# ["4","2","6","8","5","3","7","9","1"],
# ["7","1","3","9","2","4","8","5","6"],
# ["9","6","1","5","3","7","2","8","4"],
# ["2","8","7","4","1","9","6","3","5"],
# ["3","4","5","2","8","6","1","7","9"]]
# 
# Constraints:
# 
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
# 
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = {'1','2','3','4','5','6','7','8','9'}
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        tofill = []
        #filling the dicties:
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    tofill.append((i,j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3)*3 + (j//3)].add(board[i][j])
        #Backtrack algorithm here
        def backtrack():
            if len(tofill)==0:
                return True
            i,j = tofill[-1]
            for d in digits.difference(rows[i]).difference(cols[j]).difference(boxes[(i//3)*3 + j//3]):
                tofill.pop()
                board[i][j] = d
                rows[i].add(d)
                cols[j].add(d)
                boxes[(i//3)*3+j//3].add(d)
                if backtrack():
                    return True
                else:
                    tofill.append((i,j))
                    board[i][j] = '.'
                    rows[i].remove(d)
                    cols[j].remove(d)
                    boxes[(i//3)*3+j//3].remove(d)
            return False
        
        backtrack()