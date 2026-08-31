#frequency of most frequent element
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0
        total = 0
        result = 1
        
        for right in range(len(nums)):
            total += nums[right]
            
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1
            
            result = max(result, right - left + 1)
        
        return result