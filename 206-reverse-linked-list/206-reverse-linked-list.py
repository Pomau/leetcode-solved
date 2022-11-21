# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        last = None
        while node != None:
            next = node.next # 3
            node.next = last
            last = node
            node = next
        return last
            
            
        