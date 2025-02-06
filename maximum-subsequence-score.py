class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2) ]
        pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)
        sum = 0
        minHeap = []
        res = 0

        for a, b in pairs:
            sum += a
            heapq.heappush(minHeap, a)

            if len(minHeap) > k:
                toSkip = heapq.heappop(minHeap)
                sum -= toSkip
            
            if len(minHeap) == k:
                res = max(res, sum * b)

        return res
