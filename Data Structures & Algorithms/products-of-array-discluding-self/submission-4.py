class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rolling_multi = 1
        prefix = []

        for num in nums:
            rolling_multi *= num
            prefix.append(rolling_multi)

        rolling_multi = 1
        postfix = []

        for i in range(len(nums) - 1, -1, -1):
            rolling_multi *= nums[i]
            postfix.append(rolling_multi)

        postfix.reverse()

        result = []

        for i in range(len(nums)):
            left_product = prefix[i - 1] if i > 0 else 1
            right_product = postfix[i + 1] if i < len(nums) - 1 else 1

            result.append(left_product * right_product)

        return result