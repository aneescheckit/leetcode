func minCostClimbingStairs(cost []int) int {
    var costSkip []int
    var costAvail []int
    for index, val := range cost {
        if index == 0 {
            costSkip = append(costSkip, 0)
            costAvail = append(costAvail, val)
            continue
        }
        // At current step, need to figure out cost of skiping and availing the step
        costSkip = append(costSkip, costAvail[index-1])
        costAvail = append(costAvail, min(costSkip[index-1], costAvail[index-1]) + val)
    }
    return min(costSkip[len(costSkip)-1], costAvail[len(costAvail)-1])
}