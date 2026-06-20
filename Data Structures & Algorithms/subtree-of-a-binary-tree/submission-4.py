# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        
        leftSide = self.isSubtree(root.left, subRoot)
        rightSide = self.isSubtree(root.right, subRoot)

        return leftSide or rightSide

    def sameTree(self,r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            leftSide = self.sameTree(r.left, s.left)
            rightSide = self.sameTree(r.right, s.right)
            return leftSide and rightSide
        return False