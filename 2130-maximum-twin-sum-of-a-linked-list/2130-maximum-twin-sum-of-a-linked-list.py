# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        last = None
        count = 0

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            count += 1
        mid = head
        while count >= 0:
            mid = mid.next
            count -= 1
        fast = head.next
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            c = last
            last = slow
            slow = slow.next
            last.next = c
            count += 1
        slow.next = last
        ans = 0
        fast = mid
        while slow != None and fast != None:
            ans = max(ans, slow.val + fast.val)
            slow, fast = slow.next, fast.next
        return ans