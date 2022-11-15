# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head 
        while node != None:
            count += 1
            node = node.next
        return self.mergeSort(head, count)
    
    def mergeSort(self, head, count):
        if head is None:
            return None
        if count == 1:
            return head
        medium = head
        pr = head
        i = 0
        while 2 * i < count:
            pr = medium
            medium = medium.next
            i += 1
        pr.next = None
        one = self.mergeSort(head,  ceil(count / 2))
        two = self.mergeSort(medium, count//2)
        new_head = ListNode()
        node = new_head
        while one != None or two != None:
            if one != None and (two == None or one.val < two.val):
                next_node = one
                one = one.next                
            else:
                next_node = two
                two = two.next
            node.next = next_node
            node = next_node
        return new_head.next