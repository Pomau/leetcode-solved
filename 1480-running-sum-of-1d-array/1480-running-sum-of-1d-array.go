func runningSum(nums []int) []int {
    var sums []int
    for i := 0; i < len(nums); i++ {
        sums = append(sums, nums[i])
        if i != 0 {
            sums[len(sums)-1] += sums[len(sums)-2]
        }
    }
    return sums
}