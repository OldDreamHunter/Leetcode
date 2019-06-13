import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(s`elf.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]

if __name__ == '__main__':
    tempK = KthLargest(5,[2,2,2,3,4,5,9,8])
    print tempK.add(2)

