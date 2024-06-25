from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)

        for s in strs:
            # Sort the characters of the string to create a key
            sortedKey = tuple(sorted(s))
            # Add the string to the corresponding list in the dictionary
            groupedAnagrams[sortedKey].append(s)

        # Return the values of the dictionary as a list of lists
        return list(groupedAnagrams.values())