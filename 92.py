# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head and left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        curr=prev.next
        tail=curr
        prevv=None
        for _ in range(right-left+1):
            new_node=curr.next
            curr.next=prevv
            prevv=curr
            curr=new_node
        prev.next=prevv
        tail.next=curr
        return dummy.next