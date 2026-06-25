# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, 0)]
        ans = []
        while stack:
            base, height = stack.pop()
            if base is None: continue
            if len(ans) <= height: ans.append(base.val)
            ltree, rtree = base.left, base.right
            stack.append((ltree, height + 1))
            stack.append((rtree, height + 1))
        return ans