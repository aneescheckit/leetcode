class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        results = []

        def backtrack(index, cur):
            if len(cur) == len(digits):
                results.append(cur)
                return
            
            for c in maps[digits[index]]:
                backtrack(index+1, cur + c)
        
        if digits:
            backtrack(0, "")
        return results