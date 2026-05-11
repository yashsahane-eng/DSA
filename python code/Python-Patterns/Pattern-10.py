import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')
class Solution:
    
    def pattern10(self, n):
        
        for i in range(1, 2 * n):
            
            
            stars = i if i <= n else 2 * n - i
            
            
            for j in range(1, stars + 1):
                print("*", end="")
            
           
            print()

if __name__ == "__main__":
    N = int(input())
    
    
    sol = Solution()
    
    sol.pattern10(N)
