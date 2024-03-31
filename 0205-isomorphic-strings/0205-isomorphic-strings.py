class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCheck = []
        tCheck = []

        for char in s:
            sCheck.append(s.index(char))

        for char in t:
            tCheck.append(t.index(char))

        if sCheck == tCheck:
            return True
        else:
            return False