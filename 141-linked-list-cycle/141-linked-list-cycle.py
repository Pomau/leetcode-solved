# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None:
            fast = head.next
            slow = head
            while fast is not None and fast.next is not None:
                if fast == slow:
                    return True
                fast = fast.next.next
                slow = slow.next
        return False
        