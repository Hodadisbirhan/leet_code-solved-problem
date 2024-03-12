
class Solution:
    def isPalindrome(self, x: int) -> bool:
        counter=0;
        length = str(x)[::-1]
        if(str(x)==length):
            return True;
        else:
            return False;
      
            
