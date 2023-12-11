class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tmp_a, tmp_b = 0, 0
        index = 0
        for i in range(len(a)-1, -1, -1):
            tmp_a += int(a[i]) * 2**index
            index +=1
        index = 0
        for i in range(len(b) - 1, -1, -1):
            tmp_b += int(b[i]) * 2 ** index
            index += 1

        int_ans = tmp_a+tmp_b
        str_ans = ""
        if not int_ans:
            return "0"

        while int_ans:
            str_ans += str(int_ans % 2)
            int_ans = int_ans // 2


        return str_ans[::-1]

class Solution2:
    def addBinary(self, a:str, b:str)->str:
        return str(bin(int(a, base=2) + int(b, base=2)))[2:]


if __name__ == '__main__':
    sol = Solution2()
    print(sol.addBinary(a = "1101", b = "01011"))