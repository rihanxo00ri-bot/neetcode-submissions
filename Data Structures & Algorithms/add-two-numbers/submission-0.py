class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values if nodes exist, otherwise use 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Compute total and new carry
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node for the result
            curr.next = ListNode(digit)
            
            # Advance pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next