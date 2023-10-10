results = []


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.mole(root)
        global results
        results = []
        return res

    def mole(self, root):
        global results    
        if root:
            self.mole(root.left)
            results.append(root.val)
            self.mole(root.right)
        return results
