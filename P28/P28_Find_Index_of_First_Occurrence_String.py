class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            index = 0
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    tmp = ""
                    for j in range(len(needle)):
                        if needle[j] == haystack[i+j]:
                            tmp += needle[j]
                        else:
                            break
                        if tmp == needle:
                            return i
        else:
            return -1


if __name__ == '__main__':
    sol = Solution2()

    print(sol.strStr(haystack="sadbutaad", needle = "sad"))