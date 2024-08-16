class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            pp, p = 1, 2
            for i in range(3, n + 1):
                c = pp + p
                pp, p = p, c
            return c
