class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if(len(nums)==0):
            return 0
        n=sorted(nums)
        count=0
        temp=1
        for i in range(len(n)-1):
            # print(count,temp)
            if(n[i+1]-n[i]==1):
                temp+=1
            elif(n[i+1]==n[i]):
                continue
            else:
                if(count<temp):
                    count=temp
                temp=1
        return count if count > temp else temp