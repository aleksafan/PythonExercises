# K-th Symbol in Grammar https://leetcode.com/problems/k-th-symbol-in-grammar/
# On the first row, we write a 0. Now in every subsequent row, 
# we look at the previous row and replace each occurrence of 0 with 01, 
# and each occurrence of 1 with 10.

# Given row N and index K, return the K-th indexed symbol in row N. 
# (The values of K are 1-indexed.) (1 indexed).

from math import ceil, log2
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        def recGram(N: int, K: int):
            if N <= 2:
                return [0,1]
            if recGram(N-1,ceil(K/2))[(K-1)%2] == 0:
                return [0,1]   
            else:
                return [1,0]
        return recGram(ceil(log2(K))+1,ceil(K/2))[(K-1)%2]