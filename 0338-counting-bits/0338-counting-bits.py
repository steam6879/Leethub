class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        msd = 1

        for num in range(1, n + 1):
            if msd << 1 == num:
                msd = num

            dp[num] = 1 + dp[num - msd]

        return dp

