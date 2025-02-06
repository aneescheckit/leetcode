import (
    "container/heap"
)

type Item []int

func (h Item) Len() int {
    return len(h)
}

func (h Item) Less(i int, j int) bool {
    return h[i] < h[j]
}

func (h Item) Swap(i int, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *Item) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *Item) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func findKthLargest(nums []int, k int) int {
    var pqueue Item
    heap.Init(&pqueue)
    // pqueue = append(pqueue, nums[0])
    for i := 0; i < len(nums); i++ {
        heap.Push(&pqueue, nums[i])
        if pqueue.Len() > k {
            heap.Pop(&pqueue)
        }
    }
    return pqueue[0]
}