import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')


class Solution:
    
    def pattern16(self, n):
        
        for i in range(n):
            
            
            ch = chr(ord('A') + i)
            for j in range(i + 1):
                
                
                
                print(ch, end="")
                
            """ As soon as the letters for each 
            iteration are printed, we move to the
            next row and give a line break otherwise
            all letters would get printed in 1 line. """
            print()

N = int(input())


sol = Solution()

sol.pattern16(N)
