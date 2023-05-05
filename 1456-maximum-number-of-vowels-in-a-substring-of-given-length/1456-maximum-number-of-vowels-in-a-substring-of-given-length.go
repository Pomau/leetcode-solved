func maxVowels(s string, k int) int {
    vowel := []rune{'a', 'e', 'i', 'o', 'u'}
    count := 0
    ans := 0
    s_rune := []rune(s)
    for i, ch := range s_rune {
        if find_slice(vowel, ch) {
            count++
        }
        if i >= k {
            if find_slice(vowel, s_rune[i - k]) {
                count--;
            }
        }
        if count > ans {
            ans = count
        }
    }
    return ans
}
func find_slice(alf []rune, target rune) (bool) {
    for _, ch := range alf {
        if ch == target {
            return true
        }
    }
    return false;
}