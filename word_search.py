#! /usr/bin/env python

class Solution(object):
    def exists(self, board, i, j, word):
        if board[i][j] == word[0]:
            if len(word[1:]) == 0:
                return True

            board[i][j] = ' ' # update, should not used in next search
            if i-i >= 0 and self.exists(board, i-1, j, word[1:]):
                return True
            if i+i < self.m and self.exists(board, i+1, j, word[1:]):
                return True
            if j-1 >= 0 and self.exists(board, i, j-1, word[1:]):
                return True
            if j+1 < self.n and self.exists(board, i, j+1, word[1:]):
                return True
            board[i][j] = word[0] # restore
        return False


    def exist(self, board, word):
        self.m = len(board)
        if self.m==0:
            return False
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                 if self.exists(board, i, j, word):
                     return True
        return False


board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

print Solution().exist(board, "ABCCED")
print Solution().exist(board, "SEE")
print Solution().exist(board, "ABCB")
print Solution().exist(board, "ABCX")
