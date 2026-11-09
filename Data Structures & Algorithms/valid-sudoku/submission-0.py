import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hash sets to store elements seen so far in each row, column, and 3x3 box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                digit = board[r][c]
                
                # Check if the digit already exists in the current row, column, or box
                if (digit in rows[r] or 
                    digit in cols[c] or 
                    digit in squares[(r // 3, c // 3)]):
                    return False
                
                # Otherwise, add it to the respective tracking sets
                rows[r].add(digit)
                cols[c].add(digit)
                squares[(r // 3, c // 3)].add(digit)
                
        return True