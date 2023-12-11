class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([i for i in s.split(" ") if i != ""][-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord(s="Hello World"))