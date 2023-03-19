func subtractProductAndSum(n int) int {
    subtract := 1
    sum := 0
    for n > 0 {
        digit := n % 10
        n /= 10
        subtract *= digit
        sum += digit
    }
    return subtract - sum
}