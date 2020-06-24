"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
# class Solution53:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_sum = nums[0]
#         for i in range(1,n):
#             if nums[i-1] > 0:
#                 nums[i] += nums[i-1]
#             max_sum = max(nums[i], max_sum)
#         return max_sum

"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution70:
    def climbStairs(self, n: int) -> int:
        i = 0   
        nums = [0,1] 
        while i < n:
            y = nums[0] + nums[1]
            nums[0] = nums[1]
            nums[1] = y
            i += 1

        return nums[1]

# n = 2
# y = Solution70
# print (y.climbStairs(n))
"""
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. recursive solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(one, two):
            if (not one) and (not two):
                return True
            if (not one) or (not two):
                return False
            if one.val != two .val:
                return False
            return helper(one.left, two.right) and helper(one.right, two.left)
        if (not root):
            return True
        return helper (root.left, root.right)

"""
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1,root))
        depth = 0
        while stack != []:
            current_depth,root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        return depth