class Solution:
    def reverse(self, x: int) -> int:
       
            number = abs(x);
            length = len(str(number))-1;
            reverse = 0;
            while(number>0):
                remiander = number%10;
                number = number//10;
                reverse = reverse+remiander*pow(10,length);
                length = length-1;
               
            if(x<0):
                reverse= -1*reverse;
            if(reverse>=pow(-2,31) and reverse<=pow(2,31)-1):    
              return reverse;
            else:
              return 0
