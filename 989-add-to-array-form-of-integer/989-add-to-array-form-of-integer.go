func addToArrayForm(num []int, k int) []int {
    var res []int
    l := len(num) - 1
    for l >= 0 || k != 0  {
        if l >= 0 {
            k += num[l]
        }
        l--
        res = append(res, k % 10)
        k /= 10
    }
    var reverse []int
    for i := len(res) - 1; i >= 0; i-- {
        reverse = append(reverse, res[i])
    }
    return reverse
}