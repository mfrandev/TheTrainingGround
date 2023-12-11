class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]




if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums=[2,7,11,15], target=9))
