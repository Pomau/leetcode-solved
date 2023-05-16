# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_new = ListNode(0, head)
        last = head_new
        node = head_new
        while node != None and node.next != None and node.next.next != None:
            node1 = node.next
            node2 = node.next.next
            next_n = node.next.next.next
            last.next = node2
            node2.next = node1
            node1.next = next_n
            last = node1
            # print(node1.val, node2.val, last, head_new)
            node = node.next.next
        return head_new.next