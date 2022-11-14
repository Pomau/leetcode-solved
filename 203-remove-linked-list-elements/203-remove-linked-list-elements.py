# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_new = ListNode(-1, head)
        node = head_new
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head_new.next