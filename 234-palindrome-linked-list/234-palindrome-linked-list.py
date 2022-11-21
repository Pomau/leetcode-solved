# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        node = head
        while node != None:
            node = node.next
            count += 1
        m = count // 2
        middle = head
        last = None
        while m > 0:
            next = middle.next
            middle.next = last
            last = middle
            middle = next
            m -= 1
        if count % 2 == 1:
            middle = middle.next
        l = last
        r = middle
        while l != None and r != None:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True