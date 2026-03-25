class Solution(object):
    def isPalindrome(self, x):
      
      original = x
      reversed_num = 0
      if x < 0:
        return False

      while original != 0:
          dig = original%10
          reversed_num = reversed_num * 10 + dig
          original //= 10
      
      if reversed_num == x:
          return True
      else:
          return False
      
