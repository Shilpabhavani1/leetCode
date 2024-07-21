# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None: return
        curr=head
        while(curr.next):
            if curr.val==curr.next.val:
                next_node=curr.next.next
                if next_node:
                    next_node.prev=curr
                curr.next=next_node
            else:
                curr=curr.next
        return head
        