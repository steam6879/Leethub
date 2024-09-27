from collections import defaultdict
from typing import List  # Python 3.8 이하를 위한 타입 힌트


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = defaultdict(int)

        for num in nums:
            if m[num] >= 1:  # 중복 검사 수정
                return num

            m[num] += 1

        return None  # else 블록 제거