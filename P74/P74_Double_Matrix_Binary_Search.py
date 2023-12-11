class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #look at each rows bounds and see if the number is within the bounds. Then it "could" be within the matrix
        #if it is possible, then use binary search to find out if it is within the matrix.
        for row in matrix:
            lower_b, upper_b = row[0], row[-1]
            if (target >= lower_b) and (target <= upper_b):
                low_head, upper_head = 0, len(row)-1
                while (low_head <= upper_head):
                    step = (low_head + upper_head)//2
                    if row[step] > target:
                        upper_head = step-1
                    elif row[step] < target:
                        low_head = step+1
                    else:
                        return True
        return False