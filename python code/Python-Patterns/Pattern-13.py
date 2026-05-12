import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
    
    def pattern13(self, n):
        
        num = 1

        
        for i in range(1, n + 1):
            
           
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
                
            
            print()

if __name__ == "__main__":
    N = int(input())

   
    sol = Solution()

    sol.pattern13(N)
