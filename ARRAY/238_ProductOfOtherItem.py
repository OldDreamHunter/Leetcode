class Solution(object):
    def productExceptSelf(self, nums):
        if len(nums) <= 1: return nums
        product_dict = dict(zip(range(len(nums)), [[1,1]]*len(nums)))
        # product_reverse_dict = dict(zip(range(len(nums)), [1]*len(nums)))
        temp_product = 1
        temp_product_reverse = 1
        nums_reverse = nums[::-1]
        for i in range(1, len(nums)):
            temp_product = temp_product*nums[i-1]
            temp_product_reverse = temp_product_reverse*nums_reverse[i-1]
            product_dict[i][0] = temp_product
            product_dict[len(nums)-i-1][1] = temp_product_reverse
            print(product_dict)
        final_result = [product_dict[eachnum][0] * product_dict[eachnum][1] for eachnum in range(len(nums))]
        return final_result

if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([4, 3, 2]))