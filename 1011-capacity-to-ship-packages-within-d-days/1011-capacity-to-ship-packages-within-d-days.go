func shipWithinDays(weights []int, days int) int {
    l := 1
    r := int(math.Pow(10, 8))
    for (r - l > 1) {
        m := (r + l) / 2
        if (check(weights, days, m)) {
            r = m
        } else {
            l = m
        }
    }
    return r
}
func check(weights []int, days int, med int) bool {
    count := 0
    ves := 0
    for _, el := range weights {
        ves += el
        if ves > med { 
            count ++
            ves = el
        }
        if el > med {
            return false
        }
    } 
    return count <= days - 1 
}