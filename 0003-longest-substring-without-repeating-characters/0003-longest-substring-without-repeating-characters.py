class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        m = set()
        max_len = 0

        for end in range(len(s)):
            if s[end] in m:
                while s[end] in m:
                    m.remove(s[start])
                    start += 1
                
                m.add(s[end])

            else:
                m.add(s[end])
                max_len = max(max_len, end - start + 1)

        return max_len
