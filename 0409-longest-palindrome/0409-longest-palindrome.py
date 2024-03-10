from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counters = Counter(s)

        evens = [value for value in counters.values() if value % 2 == 0]
        odds = [value for value in counters.values() if value % 2 != 0]

        if odds:
            useOdds = sum(odds) - (len(odds) - 1)
            return sum(evens) + useOdds
        else:
            return sum(evens)