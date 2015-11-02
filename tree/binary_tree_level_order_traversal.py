# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        result = []
        if root is None:
            return result
        queue.append(root)
        result = [[root.val]]
        node = queue.popleft()
        count = 1
        level = []
        i = 1
        j = 0
        while node is not None:
            if node.left is not None:
                level.append(node.left.val)
                queue.append(node.left)
                j += 1
            if node.right is not None:
                level.append(node.right.val)
                queue.append(node.right)
                j += 1
            if i == count:
                i = 0
                count = j
                j = 0
                if len(level) != 0:
                    result.append(level)
                    level = []
            if len(queue) == 0:
                break
            node = queue.popleft()
            i += 1
        return result


