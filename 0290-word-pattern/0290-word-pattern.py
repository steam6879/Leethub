class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        m = {}
        
        if len(pattern) != len(sList):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in m:
                if sList[i] not in m.values():
                    m[pattern[i]] = sList[i]
                else:
                    return False
            
            else:
                if m[pattern[i]] != sList[i]:
                    return False
            
        return True