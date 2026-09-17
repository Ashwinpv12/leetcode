#find two non overlapping subarrays each with target sum
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = {0: -1}
        current_sum = 0
        min_length = float('inf')
        result = float('inf')

        for i in range(n):
            current_sum += arr[i]
            if current_sum - target in prefix_sum:
                min_length = min(min_length, i - prefix_sum[current_sum - target])
            prefix_sum[current_sum] = i

            if current_sum in prefix_sum and min_length != float('inf'):
                result = min(result, min_length + (i - prefix_sum[current_sum]))

        return result if result != float('inf') else -1