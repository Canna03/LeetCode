from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        merged_list = merged
        
        if list1 == None:
            return list2
                
        if list2 == None:
            return list1
        
        if list1.val > list2.val:
            merged.val = list2.val
            list2 = list2.next
        else:
            merged.val = list1.val
            list1 = list1.next
            
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                merged.next = ListNode(list2.val)
                list2 = list2.next
            else:
                merged.next = ListNode(list1.val)
                list1 = list1.next
            merged = merged.next
            
        while list1 != None:
            merged.next = ListNode(list1.val)
            list1 = list1.next
            merged = merged.next
            
        while list2 != None:
            merged.next = ListNode(list2.val)
            list2 = list2.next
            merged = merged.next
            
        return merged_list