import math
import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
  def CountDigits(self,n):

    if n==0:
      return 1
    
    count=0

    while n>0:
      count=count+1

      n=n//10

      return count 
    
n=int(input())

sol=Solution()

ans=sol.CountDigits(n)

print(ans)
