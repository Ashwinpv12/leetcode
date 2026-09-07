#finding missing elements in an array
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        num_set = set(nums)
        low, high = min(nums), max(nums)
        
        missing_elements = []
        for x in range(low, high + 1):
            if x not in num_set:
                missing_elements.append(x)
        
        return missing_elements