class solution(object):
    def grayCode(self,num):
        tempNumList = ['0','1']
        for i in range(num-1):
            tempNumList = self.mirror(tempNumList)
        tempNumList = list(map(lambda x:int(x,2),tempNumList))
        return tempNumList

    def mirror(self,numlist):
        mirrornums = numlist[::-1]
        nums = numlist
        mirrornums = list(map(lambda x:'1'+x,mirrornums))
        nums = list(map(lambda x:'0'+x,nums))
        numlist = nums + mirrornums
        return numlist

if __name__ == '__main__':
    problem = solution()
    print(problem.grayCode(2))

