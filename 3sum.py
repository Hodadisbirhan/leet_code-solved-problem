class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [];
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1): 
                for k in range(j+1,len(nums)):
                    value =[nums[i],nums[j],nums[k]]
                    value.sort()
                    if(nums[i]+nums[j]+nums[k] == 0 and value not in result ):
                        result.append(value)
        return result;

