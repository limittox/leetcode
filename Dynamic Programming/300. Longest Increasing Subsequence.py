"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

# O(nlogn) time complexity
class Solution:
    def lengthOfLIS(self, nums):
        def binarySearch(nums, target):
            l = 0
            r = len(nums)
            
            if len(nums) == 0:
                return 0
            
            if target > nums[len(nums)-1]:
                return len(nums)
            
            if target <= nums[0]:
                return 0
            
            
            while l <= r:
                mid = (l+r)//2
                num = nums[mid]
                
                if target == num:
                    return mid

                if nums[mid] >= target and nums[mid-1] < target:
                    return mid
                
                if target > num:
                    l = mid + 1
                else: 
                    r = mid - 1
            return -1
                    
        piles = []
        
        res = []
        
        for num in nums:
            if len(piles) == 0:
                piles.append(num)
                res.append(num)
                continue
            
            pos = binarySearch(piles, num)
            
            if pos == len(piles):
                res[-1] = piles[-1]
                piles.append(num)
                res.append(piles[-1])
            else:
                piles[pos] = num

            print(res)
        return len(piles)
            