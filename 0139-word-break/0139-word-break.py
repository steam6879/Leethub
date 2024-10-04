from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] = dp[i-len(word)]

                    if dp[i]:
                        break  # Break out as soon as you hit a true value

        return dp[-1]
