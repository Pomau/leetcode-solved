func isSubsequence(s string, t string) bool {
    l := 0
    for index, _ := range t {
        if l < len(s) && t[index] == s[l] {
            l ++
        }
    }
    return l == len(s)
}