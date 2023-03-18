# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_lenght = 0
        first_list = headA
        while first_list is not None:
            first_list = first_list.next
            first_lenght += 1
        second_lenght = 0
        second_list = headB
        while second_list is not None:
            second_list = second_list.next
            second_lenght += 1
            
        first_list = headA
        second_list = headB
        while first_lenght != second_lenght:
            if first_lenght > second_lenght:
                first_list = first_list.next
                first_lenght -= 1
            else:
                second_list = second_list.next
                second_lenght -= 1
        
        while first_list is not None:
            if first_list == second_list:
                return first_list
            first_list = first_list.next
            second_list = second_list.next
        return None