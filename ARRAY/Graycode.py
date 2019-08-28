class Solution(object):
    def grayCode(self, n):
        final_array = ['0', '1']
        while n > 1:
            final_array_reverse = final_array[::-1]
            temp_array = []
            for eachitem in final_array:
                temp_array.append(eachitem+'0')
            for eachitem in final_array_reverse:
                temp_array.append(eachitem+'1')
            final_array = temp_array
            n -= 1
        final_array = [int(eachitem,2) for eachitem in final_array]
        return final_array

if __name__ == '__main__':
    solution = Solution()
    print(solution.grayCode(5))

