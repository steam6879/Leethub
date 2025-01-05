from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            sorted_key = tuple(sorted(str))
            groups[sorted_key].append(str)

        return list(groups.values())
