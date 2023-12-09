
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # we can binary search the rows for the appropriate row, and then binary search that row itself
        lower_row, upper_row = 0, len(matrix)-1

        while lower_row <= upper_row:
            row_step = (lower_row + upper_row)//2

            #now we need to check the row that this



