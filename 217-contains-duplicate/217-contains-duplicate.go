func containsDuplicate(nums []int) bool {
    alf := make(map[int]struct{})
    for _, num := range nums {
        _, os := alf[num]
        if os {
            return true
        }
        alf[num] = struct{}{}
    }
    return false
}