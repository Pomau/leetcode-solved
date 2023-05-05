func countPrefixes(words []string, s string) int {
    ans := 0
    s_rune := []rune(s)
    for _, word := range words {
        os := true
        for i, ch := range word {
            if i >= len(s_rune) || ch != s_rune[i] {
                os = false
            }
        }
        if os {
            ans ++
        }
    }
    return ans
}