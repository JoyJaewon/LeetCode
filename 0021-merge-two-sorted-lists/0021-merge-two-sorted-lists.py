# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1, curr = list1.next, curr.next
            else:
                curr.next = ListNode(list2.val)
                list2, curr = list2.next, curr.next
        
        if list1 or list2:
            curr.next = list1 or list2
        
        return dummy.next


        