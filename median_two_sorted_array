class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        middle=0
        nums3=[];
        while(i<len(nums1) and j<len(nums2)):
           if(nums1[i]>nums2[j]):
             nums3.append(nums2[j]);
             j = j+1;
           else:
             nums3.append(nums1[i]);
             i = i+1;
                
        nums3.extend(nums1[i:]);
        nums3.extend(nums2[j:])
        middle = len(nums3)//2
        if(len(nums3)%2==0):
           
            return (nums3[middle]+nums3[middle-1])/2;
        else:
            return nums3[middle]
            
        
        
            
