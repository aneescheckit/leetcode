func tribonacci(n int) int {
    fibs := []int{0, 1, 1}
    if n == 0 {
        return 0
    }
    if n == 1 || n == 2 {
        return 1
    }

    for i := 3; i <= n; i++ {
        fibs = append(fibs, fibs[i-1] + fibs[i-2] + fibs[i-3]) 
    }

    return fibs[n]
}