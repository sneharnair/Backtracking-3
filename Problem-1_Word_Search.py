# APPROACH  1: BACKTRACKING
# Time Complexity : O(4 ^ n * m*l), n: len(word), m*l: size of the board, actually, O(3 ^n * m*l) as from every node only 3 directions will be searched as the direction 
#                   from which it came won't be searched again
# Space Complexity : O(n), as at any point the recursive stack will only have the letters in the same order of the word. 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. search through the board and if any cell equals the first letter of the word, call the backtrack function
# 2. if the pos at board and ind at word is same, mark it as # and recursively call the function in all 4 directions. as a backtrack step, set the cell back to it'soriginal letter
# 3. If at any point, pos at board and ind at word is not same, return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if board is None:
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.backtracking(board, word, row, col, 0):
                        return True
                    
        return False
    
    
    def backtracking(self, board, word, row, col, word_ind):
        # base
        if word_ind == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#':
            return False
        
        # logic 
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if board[row][col] == word[word_ind]:
            # action
            original_char = board[row][col]
            board[row][col] = '#'
            
            # recurse
            for nei in dirs:
                if self.backtracking(board, word, row + nei[0], col + nei[1], word_ind + 1):
                    return True
                
            # backtrack
            board[row][col] = original_char
            
        return False
                
                
    

                   
            
                    
