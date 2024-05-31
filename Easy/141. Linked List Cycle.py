from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ahead = head
        while ahead and ahead.next:
            head = head.next
            ahead = ahead.next.next
            if head is ahead:
                return True
        return False