# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_new = ListNode(-1005, head)
        node = head_new
        while node.next != None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head_new.next