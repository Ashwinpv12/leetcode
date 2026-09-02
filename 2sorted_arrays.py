#to find the median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n == 0:
            return None
        middle = n//2

        if n % 2 ==1:
            return merged[middle]

        else:
            return (merged[middle-1] + merged[middle]) /2    
