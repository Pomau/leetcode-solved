# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        count = 0
        while node != None:
            count += 1
            node = node.next
        middle = count // 2
        head_new = head
        while middle > 0:
            head_new = head_new.next
            middle -= 1
        return head_new