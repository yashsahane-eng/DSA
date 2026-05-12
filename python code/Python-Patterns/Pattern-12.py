import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')
class Solution:
    
    def pattern12(self, n):
        
        spaces = 2 * (n - 1)

        
        for i in range(1, n + 1):
            
            for j in range(1, i + 1):
                print(j, end="")

            
            for j in range(1, spaces + 1):
                print(" ", end="")

           
            for j in range(i, 0, -1):
                print(j, end="")

            
            print()

            
            spaces -= 2

if __name__ == "__main__":
    N = int(input())

  
    sol = Solution()

    sol.pattern12(N)
