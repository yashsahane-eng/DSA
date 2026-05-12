import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')
class Solution:
    
    def pattern15(self, n):
        
        for i in range(n):
            
            
            for ch in range(ord('A'), ord('A') + n - i):
                print(chr(ch), end="")
                
            
            print()

if __name__ == "__main__":
    N = int(input())

   
    sol = Solution()

    sol.pattern15(N)
