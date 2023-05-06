func numSubseq(nums []int, target int) int {
    sort.Ints(nums)
    pows := make([]int, len(nums))
    pows[0] = 1 
    mod := int(math.Pow(10, 9)) + 7 
    for i := range pows {
        if i == 0 {
            continue
        }
        pows[i] = (pows[i - 1] * 2) % mod
    }
    ans := 0
    for i, num := range nums {
        l, r := i, len(nums)
        for {
            if r - l <= 1 {
                break
            }
            m := (r + l) / 2
            if nums[m] + num > target {
                r = m
            } else {
                l = m
            }
        }
        if nums[l] + num <= target {
            ans = (ans + pows[l - i]) % mod
        }
       
    }
    return ans
}