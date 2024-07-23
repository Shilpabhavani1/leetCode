class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        temp=ListNode(0)
        curr=temp
        while l1 or l2 or carry!=0:
            v1=l1.val if l1 is not None else 0
            v2=l2.val if l2 is not None else 0
            total=v1+v2+carry
            carry=total//10
            new_node=ListNode(total%10)
            curr.next=new_node
            curr=curr.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        return temp.next