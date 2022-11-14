# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_new = ListNode(-1, head)
        prew_node = head_new
        node = head_new.next
        while node is not None:
            while node is not None and node.val == val:
                node = node.next
            prew_node.next = node
            prew_node = node
            if node is not None:
                node = node.next
        return head_new.next