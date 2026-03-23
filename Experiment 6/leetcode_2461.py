class Solution(object):
    def maximumSubarraySum(self, nums, k):
        freq = {}
        left = 0
        curr_sum = 0
        max_sum = 0        
        for right in range(len(nums)):
            curr_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1            
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                curr_sum -= nums[left]
                left += 1                        
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, curr_sum)       
        return max_sum
