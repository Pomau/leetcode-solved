# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            answer = []
            for i in range(1, len(lists), 2):
                answer.append(self.merge(lists[i], lists[i - 1]))
            if len(lists) % 2 == 1:
                answer.append(lists[-1])
            lists = answer
        if len(lists) > 0:
            return lists[0]
        return None
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1 != None:
            node.next = list1
        if list2 != None:
            node.next = list2
        return head.next