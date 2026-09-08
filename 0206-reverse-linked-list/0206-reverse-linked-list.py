class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next   # save next node
            curr.next = prev        # reverse the link
            prev = curr             # move prev forward
            curr = next_temp        # move curr forward
        
        return prev  # new head