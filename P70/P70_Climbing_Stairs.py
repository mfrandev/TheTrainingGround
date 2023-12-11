class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        for a given n, we need to find the number of steps needed to reach the top. The steps taken at any moment can either be 1 or 2. We need to
        find the number of combinations between all step choices.
        :param n: # of steps
        :return: numbers of combinations

        say we had 10
        we can have 2 x 5
                    1+1+2x4

        2 + 2 + 2 + 2 + 2
        1 + 1 + 2 + 2 + 2 + 2
        1 + 2 + 1 + 2 + 2 + 2
        '''
        sol = n%2
        if sol == 0:
            print(f"{n} | {sol}")
            print(n//2)
        else:
            print(f"{n} | {n-1} | {sol}")

        return 0

    def recursion(self, n):

        if n<=1:
            return 1
        return n * self.recursion(n=n-1)
