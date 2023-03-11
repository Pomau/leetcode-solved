# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        count = 0
        while node != None:
            node = node.next
            count += 1
        return self.dfs(head, 0, count)
    
    def dfs(self, root, l, r):
        if l >= r:
            return None
        if r - l == 1:
            return TreeNode(root.val)
        m = (r + l) // 2
        node = root
        count = l
        while count < m:
            node = node.next
            count += 1
        l = self.dfs(root, l, m)
        r = self.dfs(node.next, m + 1, r)
        return TreeNode(node.val, l, r)
        