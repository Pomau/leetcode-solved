# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node != None:
            node = node.next
            count += 1
        number = count - n
        head_new = ListNode(-1, head)
        node = head_new
        for i in range(number):
            node = node.next
        node.next = node.next.next
        return head_new.next