# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if root is None: return ans
        stack = [(root, root.val)]

        while stack:
            base, tracker = stack.pop()
            if base is None: continue
            if tracker <= base.val: ans += 1
            stack.append((base.left, max(tracker, base.val)))
            stack.append((base.right, max(tracker, base.val)))
        return ans
            