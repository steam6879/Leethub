from collections import Counter


class Solution(object):
    def characterReplacement(self, s, k):
        maxLength, maxCount = 0, 0
        counters = Counter()

        for i in range(len(s)):
            counters[s[i]] += 1
            maxCount = max(maxCount, counters[s[i]])

            if maxLength - maxCount >= k:
                counters[s[i - maxLength]] -= 1

            else:
                maxLength += 1

        return maxLength