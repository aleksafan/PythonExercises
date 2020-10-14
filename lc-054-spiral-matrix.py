# Spiral matrix https://leetcode.com/problems/spiral-matrix/
# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        def right(matrix): 
            return matrix.pop(0)
        def left(matrix):
            return matrix.pop(-1)[::-1]
        def down(matrix):
            return [x.pop(-1) for x in matrix]
        def up(matrix):
            return [x.pop(0) for x in matrix][::-1]
        
        while matrix and matrix[0]:
            for func in [right, down,left,up]:
                if matrix and matrix[0]:
                    res += func(matrix)
                else:
                    break
    
        return res