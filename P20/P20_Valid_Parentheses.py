class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        #here we are going to use a stack to stack the number of open brackets. If we come across a close bracket, we then need to make sure that
        # the appropriate open bracket precedes it. If not, it fails. If the stack has a length > 0, it fails. Else it passes
        if s[0] not in par_dict:
            return False


        stack = []
        for i in range(0, len(s), 1):
            if s[i] in par_dict: #is we come across a open bracket, append it to the stack
                stack.append(s[i])
            else: #we come across a close bracket
                try:
                    if s[i] != par_dict[stack.pop()]:
                        return False
                except:
                    stack.append(s[i])

        if len(stack):
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(s="(){}}{"))
