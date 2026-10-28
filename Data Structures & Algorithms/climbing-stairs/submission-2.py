class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        for i in range(2,n):
            temp = one
            temp2 = two
            two = one + two
            one = temp2
        return 1 if n == 1 else two