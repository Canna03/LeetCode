from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_list = None
        while head:
            next_node = head.next
            head.next = reverse_list
            reverse_list = head
            head = next_node
        return reverse_list

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(Solution().reverseList(node))
            