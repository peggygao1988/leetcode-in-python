# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.dfs(root)

    def dfs(self, node):
        if node.left is None and node.right is None:
            return 1

        left_depth = right_depth = 0
        if node.left is not None:
            left_depth = self.dfs(node.left)
        if node.right is not None:
            right_depth = self.dfs(node.right)

        if left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        else:
            return min(left_depth, right_depth) + 1
