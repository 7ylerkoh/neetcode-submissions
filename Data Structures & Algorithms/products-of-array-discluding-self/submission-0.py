class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_count = 1, 0
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        answer = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                answer[i] = 0 if num else product
            else:
                answer[i] = product // num
        
        return answer