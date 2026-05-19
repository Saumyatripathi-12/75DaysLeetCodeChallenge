class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # If root is None or matches p or q
        if not root or root == p or root == q:
            return root

        # Search in left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return a node, root is LCA
        if left and right:
            return root

        # Otherwise return non-null node
        return left if left else right
        