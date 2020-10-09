# Diagonal Traverse https://leetcode.com/problems/diagonal-traverse/
# Given a matrix of M x N elements (M rows, N columns), 
# return all elements of the matrix in diagonal order 

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        upright = True
        i = j = 0
        while i<len(matrix) and j<len(matrix[0]):
            res.append(matrix[i][j])
            if upright:
                while i>0 and j<len(matrix[0])-1:
                    i-=1
                    j+=1
                    res.append(matrix[i][j])
                if j < len(matrix[0]) - 1:
                    j+=1
                else:
                    i+=1
                upright = False
            else:
                while j>0 and i<len(matrix)-1:
                    i+=1
                    j-=1
                    res.append(matrix[i][j])
                if i<len(matrix)-1:
                    i+=1
                else:
                    j+=1
                upright = True
        return res                