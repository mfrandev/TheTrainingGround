class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        tmp = ""
        for i in digits:
            tmp += str(i)

        tmp_num = int(tmp) + 1
        return [int(i) for i in str(tmp_num)]


if __name__ == '__main__':
    sol = Solution()

    print(sol.plusOne(digits=[9]))
