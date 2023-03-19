func average(salary []int) float64 {
    sums := 0.
    min_el := float64(salary[0])
    max_el := min_el
    for _, element := range salary {
        sums += float64(element)
        min_el = math.Min(min_el, float64(element))
        max_el = math.Max(max_el, float64(element))
    }
    return (sums - min_el - max_el) / float64(len(salary) - 2)
}