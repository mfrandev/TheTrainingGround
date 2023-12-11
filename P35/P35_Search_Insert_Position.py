class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        if nums[low] >= target:
            return low
        elif nums[high] < target:
            return high + 1
        elif nums[high] == target:
            return high
        else:

            x = 0
            while x < len(nums):
                step = (high + low) // 2
                if nums[step] == target:
                    return step
                elif nums[step] < target:
                    low = step+1

                else:
                    high = step-1

                x += 1

        if step == low:
            return step + 1
        elif step == high:
            return high + 1

class Solution2:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            step = (left + right)//2
            if nums[step] > target:
                right = step-1
            elif nums[step] < target:
                left = step+1
            else:
                return step
        return left


if __name__ == '__main__':
    sol = Solution2()
    print(sol.searchInsert(nums=[2,3,5,6,9], target=7))