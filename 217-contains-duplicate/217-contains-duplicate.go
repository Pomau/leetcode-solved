func containsDuplicate(nums []int) bool {
    alf := make(map[int]bool)
    for _, num := range nums {
        os, _ := alf[num]
        if os {
            return true
        }
        alf[num] = true
    }
    return false
}