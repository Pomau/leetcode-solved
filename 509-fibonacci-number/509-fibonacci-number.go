func fib(n int) int {
    now, next := 0, 1
    for i := 0; i < n; i++ {
        now, next = next, now + next
    }
    return now
}