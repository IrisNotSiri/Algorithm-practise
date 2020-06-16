"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(1,n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)
        return max_sum

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

n = 2
y = Solution70
print (y.climbStairs(n))