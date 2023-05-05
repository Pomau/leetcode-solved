/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
    ans := [][]int{}
    dfs(root, 0, &ans)
    for i := 1; i < len(ans); i += 2 {
        for j:= 0; j < len(ans[i]) / 2; j++ {
            ans[i][j], ans[i][len(ans[i]) - j - 1] = ans[i][len(ans[i]) - j - 1], ans[i][j]
        }
    }
    return ans
}
func dfs(root *TreeNode, depth int, ans *[][]int) {
    if root == nil {
        return
    }
    if len(*ans) <= depth {
        *ans = append(*ans, []int{(*root).Val})
    } else {
        (*ans)[depth] = append((*ans)[depth], (*root).Val)
    }
    dfs((*root).Left, depth + 1, ans)
    dfs((*root).Right, depth + 1, ans)
}