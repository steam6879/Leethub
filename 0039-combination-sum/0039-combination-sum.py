class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            for i in range(start, len(candidates)):
                current = candidates[i]
                if current > remaining:
                    break
                combo.append(current)
                backtrack(remaining - current, combo, i)
                combo.pop()
        
        backtrack(target, [], 0)
        return result