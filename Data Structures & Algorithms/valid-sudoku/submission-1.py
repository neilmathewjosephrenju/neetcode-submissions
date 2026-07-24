from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check all rows
        for row in range(9):
            seen = set()

            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check all columns
        for col in range(9):
            seen = set()

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check all 3x3 boxes
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):

                seen = set()

                for row in range(boxRow, boxRow + 3):
                    for col in range(boxCol, boxCol + 3):

                        value = board[row][col]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True