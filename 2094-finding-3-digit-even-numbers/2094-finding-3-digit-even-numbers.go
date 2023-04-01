func findEvenNumbers(digits []int) []int {
    used := make(map[int]bool)
    for i := 0; i < len(digits); i++ {
        if digits[i] == 0 {
            continue
        }
        for y := 0; y < len(digits); y++ {
            if y == i {
                continue
            }
            for z := 0; z < len(digits); z++ {
                if digits[z] % 2 == 1 || i == z || y == z {
                    continue
                }
                nums := digits[i] * 100 + digits[y] * 10 + digits[z]
                _, have := used[nums]
                if have {
                    continue
                }
                used[nums] = true
            }
        }
    }
    ans := []int{}
    for key, _ := range used {
        ans = append(ans, key)
    }
    sort.Ints(ans)
    return ans
    
}