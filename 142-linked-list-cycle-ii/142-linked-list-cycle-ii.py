# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        slow = head.next
        fast = slow.next
        while fast != None and fast.next != None and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if fast == None or fast.next == None:
            return None
        node = head
        while node != slow:
            node = node.next
            slow = slow.next
        return node
        