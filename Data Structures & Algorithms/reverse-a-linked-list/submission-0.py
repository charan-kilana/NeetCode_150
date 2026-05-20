# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Brute Force Method
        new = []
        for i in range(len(head)-1,0):
            new.append(head[i]) 
        return new