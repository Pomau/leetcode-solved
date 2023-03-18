func isIsomorphic(s string, t string) bool {
    alf := make(map[byte]byte)
    used := make(map[byte]bool)

    for index, _ := range s {
        el := s[index]
        replace, have_alf := alf[el]
        if (!have_alf) {
            replace = t[index]
            _, have_used := used[replace]
            if (have_used) {
                return false
            }
            alf[el] = replace
            used[replace] = true
        }
        if replace != t[index] {
            return false
        }
    }
    return true

}