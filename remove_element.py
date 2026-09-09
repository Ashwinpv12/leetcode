#given element from a given array and print the element after removing the given element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      k=0  
      for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+=1

      return k     