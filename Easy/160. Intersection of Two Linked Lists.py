from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA, lengthB = 0, 0
        tailA, tailB = headA, headB
        
        while tailA.next:
            lengthA += 1
            tailA = tailA.next
        while tailB.next:
            lengthB += 1
            tailB = tailB.next
        if not tailA == tailB:
            return None

        if lengthA > lengthB:
            for _ in range(lengthA - lengthB):
                headA = headA.next
        elif lengthA < lengthB:
            for _ in range(lengthB - lengthA):
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None