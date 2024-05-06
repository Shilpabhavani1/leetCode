class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(inf)
        stack = [dummy]
        
        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next
        
        return dummy.next