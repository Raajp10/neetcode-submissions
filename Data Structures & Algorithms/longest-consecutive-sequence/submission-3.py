class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # nlog(n) with sort 
        # if(len(nums)==0):
        #     return 0
        # n=sorted(nums)
        # count=0
        # temp=1
        # for i in range(len(n)-1):
        #     # print(count,temp)
        #     if(n[i+1]-n[i]==1):
        #         temp+=1
        #     elif(n[i+1]==n[i]):
        #         continue
        #     else:
        #         if(count<temp):
        #             count=temp
        #         temp=1
        # return count if count > temp else temp

        
        hashset = set(nums)
        max_count=0
       
        for i in hashset:
            if i-1 not in hashset:
                current = i
                streak = 1
                while current + 1 in hashset:
                    current += 1
                    streak += 1

                max_count = max(max_count, streak)

        return max_count