func pivotIndex(nums []int) int {
    prefix := 0
    suffix := 0
    for _, el := range nums {
        suffix += el
    }

    for index, el := range nums {
        suffix -= el
        if prefix == suffix {
            return index
        }
        prefix += el
    }
    return -1
}