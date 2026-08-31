#container with the most water
'''
def max_area(height):
    left = 0 
    right =  len(height) -1
    max_area =0
    while left <right:
        width = right - left
        current_area = min(height[left], height[right])
        area = width * current_area
        max_area = max(max_area, area)
        
    return max_area    '''
    
    
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right =  len(height) -1
        max_area =0
        while left <right:
            width = right - left
            current_area = min(height[left], height[right])
            area = width * current_area
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area