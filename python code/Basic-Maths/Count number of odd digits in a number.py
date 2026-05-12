import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')


class Solution:
  def countOddDigits(self, n):

    oddDigits=0

    while n>0:

      lastDigits=n%10

      if lastDigits%2!=0:
        oddDigits+=1
      n=n//10

    return oddDigits
  
n=int(input())
sol = Solution()


ans = sol.countOddDigits(n)
print("The count of odd digits in the given number is:", ans)

