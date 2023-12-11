class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        for i, val in enumerate(unique):
            nums[i] = val

        for j in range(len(unique), len(nums), 1):
            nums[j] = "_"
        return len(unique)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
