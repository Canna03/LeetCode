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
        
        reverse
        