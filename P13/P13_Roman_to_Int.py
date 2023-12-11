class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        spec_roman = {
            'IV': [4, 1], #extra 1
            'IX': [9, 1], #extra 1
            'XL': [40, 20], #extra 20
            'XC': [90, 20], # extra 20
            'CD': [400, 200], # extra 200
            'CM': [900, 200] #extra 200
        }
        return_int = 0
        for k, v in spec_roman.items():
            if k in s:
                return_int += v[0]
                s = s.replace(k, "")

        for i in range(0, len(s), 1):
            return_int += rom_to_int[s[i]]
        return return_int



        # return_int = 0
        # for i in range(0, len(s), 1):
        #     return_int += rom_to_int[s[i]]
        #     print(return_int)
        # for k, v in spec_roman.items():
        #     if k in s:
        #         print(k)
        #         return_int -= v[1]
        #
        # return return_int

if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt(s="MCMXCIV"))
