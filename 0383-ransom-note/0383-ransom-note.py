from collections import defaultdict, Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for char in ransomNote:
            if not counter[char]:
                return False

            counter[char] -= 1

        return True
