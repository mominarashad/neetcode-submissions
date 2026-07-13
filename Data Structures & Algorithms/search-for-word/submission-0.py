class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def solve(r, c, index):
            # matched all letters
            if index == len(word):
                return True

            # out of bounds, or cell doesn't match, or already used in this path
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or board[r][c] != word[index]):
                return False

            # mark this cell as visited (in-place, saves memory vs a separate set)
            temp = board[r][c]
            board[r][c] = "#"

            found = (solve(r+1, c, index+1) or
                     solve(r-1, c, index+1) or
                     solve(r, c+1, index+1) or
                     solve(r, c-1, index+1))

            # backtrack: restore the cell so other paths can use it
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if solve(r, c, 0):
                    return True

        return False