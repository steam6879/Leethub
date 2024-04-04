class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr, tPtr = 0, 0
        while tPtr < len(t) and sPtr < len(s):
            if s[sPtr] == t[tPtr]:
                sPtr += 1
                
            tPtr += 1

        return sPtr == len(s)