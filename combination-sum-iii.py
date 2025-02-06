class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(index, curr, s):
            if len(curr) == k or index > 9:
                if len(curr) != k:
                    return
                if s == n:
                    results.append(curr.copy())
                return
            
            curr.append(index)
            backtrack(index+1, curr, s + index)
            curr.pop()
            backtrack(index+1, curr, s)
        
        backtrack(1, [], 0)
        return results
