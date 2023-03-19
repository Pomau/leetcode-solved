func countOdds(low int, high int) int {
    return (high - low + 1 - (low % 2)) / 2 + (low % 2)
}
// 5 10 5 -> 5 7 9
// 5 9 4 -> 5 7 9
// 6 10 4 -> 7 9
// 6 9 3 -> 7 9