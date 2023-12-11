class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index+=1
        return index



if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 2, 3]
    print(sol.removeElement(nums = nums, val=3))
    print(nums)