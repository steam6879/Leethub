class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        resS = []
        resT = []

        for char in list(s):
            if char != '#':
                resS.append(char)
            else:
                if not resS:
                    continue
                resS.pop()

        for char in list(t):
            if char != '#':
                resT.append(char)
            else:
                if not resT:
                    continue
                resT.pop()

        return resS == resT