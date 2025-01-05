from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s, p):
        ans = []
        p_counter = Counter(p)
        s_counter = Counter(s[ : len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            start_index = i - len(p) + 1
            s_counter[s[i]] += 1

            if s_counter == p_counter:
                ans.append(start_index)  # start index.

            s_counter[s[start_index]] -= 1

            if s_counter[s[start_index]] == 0:
                del s_counter[s[start_index]]

        return ans
