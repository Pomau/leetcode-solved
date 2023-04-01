func targetIndices(nums []int, target int) []int {
    var ans []int
    k := 0
    for i := 0; i < len(nums); i ++ {
        if nums[i] < target {
            k ++
        }
    }
    for i := 0; i < len(nums); i++ {
        if nums[i] == target {
            ans = append(ans, k)
            k += 1
        }
    }
    return ans
}