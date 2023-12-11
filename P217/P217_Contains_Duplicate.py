class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #if list(set(nums)) == nums:
        #     return False
        # return True
        return False if sorted(list(set(nums))) == sorted(nums) else True


if __name__ == '__main__':
    print(Solution().containsDuplicate(nums=[1,5,-2,-4,0]))
