
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def best(root):
            if root not in dp:
                dp[root] = max(
                    best0(root), 
                    root.val + best0(root.left) + best0(root.right)
                )

            return dp[root]
            
        def best0(root):
            return best(root.left) + best(root.right) if root else 0

        dp = {None:0}
        return best(root)

