class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        slist = list(s)
        n = len(slist)
        s_table = {}
        r = -1

        for i in range(n):
            if slist[i] in s_table:
                r = max(r, i - s_table[slist[i]] - 1)
            else:
                s_table[slist[i]] = i
                
        return r