from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def subtreeSymmetric(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 == None and root2 == None:
                return True
            
            elif root1 == None or root2 == None:
                return False
            
            if root1.val != root2.val:
                return False
            
            return subtreeSymmetric(root1.left, root2.right) and subtreeSymmetric(root2.left, root1.right)

        return subtreeSymmetric(root.left, root.right)