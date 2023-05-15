/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapNodes(head *ListNode, k int) *ListNode {
    count := 0
    node := head
    for node != nil {
        count++
        node = node.Next
    }
    target := head
    target2 := head
    node = head
    for i := 1; i <= count; i++ {
        if i == k {
            target = node
        } 
        if i == count - k+1 {
            target2 = node
        }
        node = node.Next
    }
    
    target.Val, target2.Val =  target2.Val, target.Val
    return head
    
    
}