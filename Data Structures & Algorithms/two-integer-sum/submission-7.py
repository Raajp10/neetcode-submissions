class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             return [i,j]
        # return [-1]

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(target-nums[i]==nums[j]):
        #             return[i,j]
        #         if(target-nums[i]>0):
        #             continue

        
        hashset={}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashset:
                return [hashset[diff],i]
            
            hashset[num]=i
            