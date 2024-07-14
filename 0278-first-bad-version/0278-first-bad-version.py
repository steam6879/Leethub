# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        pl, pr = 1, n

        while pl <= pr:
            pc = (pl + pr) // 2

            if isBadVersion(pc):
                pr = pc - 1
            else:
                pl = pc + 1

        return pl