from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # l1 to half
        l1 = head
        l2 = head
        while l2.next and l2.next.next:
            l1 = l1.next
            l2 = l2.next.next
        
        if l2.next:
            l2 = l1.next.next
        
        reverse = head
        temp = head.next
        while reverse != l1:
            reverse.next = None
            reverse = temp
            temp = temp.next
        
        
        while l1.next:
            if l1.val != reverse.val:
                return False
            l1 = l1.next
            reverse = reverse.next
        
        return True
        
        