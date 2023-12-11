class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # we can binary search the rows for the appropriate row, and then binary search that row itself
        row_list = [val[0] for val in matrix]
        low_row, high_row = 0, len(row_list) - 1
        print(row_list)

        while low_row <= high_row:
            row_step = (low_row + high_row) // 2
            if row_list[row_step] > target:
                high_row = row_step-1
            elif row_list[row_step] < target:
                low_row = row_step+1
            else:
                break

        if row_step > high_row:
            row = matrix[high_row]
        else:
            row = matrix[row_step]


        col_low, col_high = 0, len(row) - 1
        while col_low <= col_high:
            col_step = (col_low + col_high) // 2
            if row[col_step] > target:
                col_high = col_step - 1
            elif row[col_step] < target:
                col_low = col_step + 1
            else:
                return True
        return False




