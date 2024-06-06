class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for char in s:
            if char in m:
                m[char] += 1

            else:
                m[char] = 1

        for char in t:
            if char in m:
                m[char] -= 1
                if m[char] < 1:
                    m.pop(char)

            else:
                return False

        return len(m) == 0
