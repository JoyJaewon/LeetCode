# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
input: An array of k linked lists sorted in ascending order
output: Sigle sorted linked list

Clarifications
- will the length of each list be the same? No
- can lists be empty? Yes
- if all input linked-lists are empty, what should be returned? empty linked list

Test Cases
[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
[] -> []
[[]] -> []

Approach 1) Brute Force - combine all the value of the linked lis into the list. sort. make new LL
            O(nlogn)
Approach 2) Min Heap - keep track of the smallest element across all linked lists

Plan
- define the function taking lists as parameter
    - initialize heap to empty list
    - go through the linked list. add the first value to the heap (val, index, list)
    - initialize dummy node and have curr points to dummy node
    - while heap:
        - pop the node
        - curr.next = node
        - curr = curr.next
        - if there is the next node, put the next element into the heap
    - return dummy.next

TC: O(Nlogk), SC: O(K)
'''
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, l = heapq.heappop(heap)
            curr.next = l
            curr = curr.next
            if l.next:
                heapq.heappush(heap, (l.next.val, i, l.next))
        
        return dummy.next
        