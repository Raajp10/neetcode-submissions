class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # answer=[]
        # nums.sort()
        # # Brute force with O(n^3)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if (nums[i]+nums[j]+nums[k]==0):
        #                 x = [nums[i],nums[j],nums[k]]
        #                 if x not in answer:
        #                     answer.append(x)
        # return answer

        answer = []
        nums.sort()
        
        for i in range(len(nums)):
            if (nums[i]==nums[i-1]) and (i > 0):
                continue
            
            left=i+1
            right=len(nums)-1

            while(left < right):
                curr = nums[i] + nums[left] + nums[right]

                if(curr == 0):
                    x=[nums[i],nums[left],nums[right]]
                    right-=1
                    if x not in answer:
                        answer.append(x)
                elif (curr < 0):
                    left+=1
                else:
                    right-=1
        return answer
