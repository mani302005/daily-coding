# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import permutations
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp =[[None]*(n+1) for i in range(n+1)]
        def du(s,e):
            if s >e:
                return [None]
            if dp[s][e] is not None:
                return dp[s][e]
            ans = []
            for r in range(s,e+1):
                ln = du(s,r-1) 
                rn = du(r+1,e)
                for i in ln:
                    for j in rn :
                       node = TreeNode(r)
                       node.left = i
                       node.right = j
                       ans.append(node)
            dp[s][e] = ans
            return dp[s][e]
            
        return du(1,n)
        