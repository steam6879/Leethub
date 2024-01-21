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
            else:
                return False
            
        for char in m:
            if m[char] != 0:
                return False
        
        return True