import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.record = {}
        self.sortedElements = []
        for i in range(1, 1001):
            self.sortedElements.append(i)
            self.record[i] = True

        heapq.heapify(self.sortedElements)

    def popSmallest(self) -> int:
        if len(self.sortedElements) > 0:
            element = heapq.heappop(self.sortedElements)
            self.record[element] = False
            return element
        

    def addBack(self, num: int) -> None:
        if not num in self.record or (num in self.record and not self.record[num]):
            self.record[num] = True
            heapq.heappush(self.sortedElements, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)