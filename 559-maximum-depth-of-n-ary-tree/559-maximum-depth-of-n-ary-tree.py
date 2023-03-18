"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        answer = 0
        for child in root.children:
            answer = max(answer, self.maxDepth(child))
        return answer + 1