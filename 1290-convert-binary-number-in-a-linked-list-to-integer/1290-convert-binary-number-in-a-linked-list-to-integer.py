# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = 0
        node = head
        while node != None:
            nums = nums * 2 + node.val
            node = node.next
        return nums