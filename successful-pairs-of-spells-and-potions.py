class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binarySearch(spell):
            l, r = 0, len(potions) - 1
            index = len(potions)
            while l <= r:
                m = (l + r) // 2
                if spell * potions[m] >= success:
                    r = m - 1
                    index = m
                else:
                    l = m + 1
            return len(potions) - index
        
        return [binarySearch(spell) for spell in spells]
