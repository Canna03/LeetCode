from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        merged_list = merged
        if list1.val > list2.val:
            merged.val = list2.val
        else:
            merged.val = list1.val
        while list1.next != None or list2.next != None:
            if list1.val > list2.val:
                merged.next = ListNode(list2.val)
            else:
                merged.next = ListNode(list1.val)
            merged = merged.next
        return merged_list