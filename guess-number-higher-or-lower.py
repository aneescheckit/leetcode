/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    // Range is 0 to n
    fmt.Println("Start", n)
    min := 1
    max := n
    ans := max
    for min < max {
        ans = int(math.Floor(float64((min+max)/2)))
        num := guess(ans)
        if num == 0 {
            break
        } else if num < 0 {
            max = ans - 1
        } else {
            min = ans + 1
        }
    }
    return ans
}