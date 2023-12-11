import math
class Solution:
    def mySqrt(self, x: int) -> int:

        #we are going to be implementing a binary search to speed up our brute force search.
        if x == 1:
            return 1

        low, high = 0, x
        step = 0
        index = 0
        while low <= high:
            mid = (low + high)//2
            if mid**2 < x:
                low = mid+1
            elif mid**2 > x:
                high = mid-1
            else:
                return mid
        return high





if __name__ == '__main__':
    sol = Solution()
    print(sol.mySqrt(x = 2147395599))