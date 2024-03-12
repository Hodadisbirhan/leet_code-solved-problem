class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height) - 1
        maxCont = float('-inf')
        while i < j:
            maxCont = max(maxCont, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxCont
#          length = len(height);
#          counter = length-1;
#          i=0
#          if(height[0]>height[counter]):
#             maximum = counter*height[counter];
#          else:
#             maximum = counter*height[0];
            
       
#          while(i<length-1):
#            counter=length-1-i;
#            j=length-1;
#            temp_counter=counter; 
#            while(j>i):
#             if(height[i]<=height[j]):
#               calculate =height[i]*temp_counter;
#               if(maximum<calculate):
#                 maximum = calculate;
#               break;
#             else:
#                 calculate =height[j]*temp_counter;
#                 if(maximum<=calculate):
#                     maximum = calculate;
#                 j = j-1;
#                 temp_counter = temp_counter-1;
#            i=i+1
#          return maximum;
                
                
                    
             
                    
