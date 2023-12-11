class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return_str = ""
        short_str = sorted(strs, key=len)[0]
        for i in range(0, len(short_str), 1):
            tmp = 
            for word in strs:




if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(strs=["flower","flow","flight"]))