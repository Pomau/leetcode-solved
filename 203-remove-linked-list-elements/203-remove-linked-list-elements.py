# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_new = head
        while head_new is not None and head_new.val == val:
            head_new = head_new.next
        prew_node = head_new
        node = head_new
        if head_new is not None:
            node = head_new.next
        while node is not None:
            while node is not None and node.val == val:
                node = node.next
            prew_node.next = node
            prew_node = node
            if node is not None:
                node = node.next
        return head_new