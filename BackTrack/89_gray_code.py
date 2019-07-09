class solution(object):
    def gray(self, num):
        res = []
        self.backtrack(num,0,[],res)

    def backtrack(self,num,index,path,res):
        if len(path) == num: res.append(path)
        for eachnum in ['0','1']:


