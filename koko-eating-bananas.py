class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1] # max number
        currentMinCount = float("inf")
        while l <= r:
            m = (l + r) // 2
            hour = 0
            for i in piles:
                div = (i // m)
                if i % m != 0:
                    div += 1
                hour += div
            print(div, hour)
            if hour <= h:
                if m < currentMinCount:
                    currentMinCount = m
                r = m - 1
            elif hour > h:
                l = m + 1
            else:
                r = m - 1
        
        return currentMinCount