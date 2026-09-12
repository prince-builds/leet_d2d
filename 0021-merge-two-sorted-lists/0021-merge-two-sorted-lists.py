class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)      # Fake start node
        current = dummy          # Pointer to build the list
        
        while list1 and list2:   # While BOTH lists have nodes
            if list1.val <= list2.val:
                current.next = list1   # Attach list1's node
                list1 = list1.next     # Move list1 forward
            else:
                current.next = list2   # Attach list2's node
                list2 = list2.next     # Move list2 forward
            current = current.next     # Move current forward
        
        # Attach remaining nodes (one list is now empty)
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next        # Return the merged list (skip dummy)