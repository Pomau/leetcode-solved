# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        transfer = 0
        head = ListNode()
        node = head
        while l1 != None or l2 != None or transfer > 0:
            if l1 != None:
                transfer += l1.val
                l1 = l1.next
            if l2 != None:
                transfer += l2.val
                l2 = l2.next
            node.next = ListNode(transfer % 10)
            node = node.next
            transfer //= 10
        return head.next