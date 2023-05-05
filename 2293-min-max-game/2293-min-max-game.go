func min(a, b int) (int) {
    if a > b {
        return b
    }
    return a
}
func max(a, b int) (int) {
    if a > b {
        return a
    }
    return b
}

func minMaxGame(nums []int) int {
    count := len(nums)
    for {
        if count == 1 {
            break
        }
        count /= 2
        for i := 0; i < count; i++ {
            if i % 2 == 0 {
                nums[i] = min(nums[2 * i], nums[2 * i + 1])
            } else {
                nums[i] = max(nums[2 * i], nums[2 * i + 1])
            }
        }
    }
    return nums[0]
}
