import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')
class Solution:
    def pattern9(self, n):
        self.erect_pyramid(n)
        self.inverted_pyramid(n)

    def erect_pyramid(self, n):
        
        for i in range(n):
            
            for j in range(n - i - 1):
                print(" ", end="")

            
            for j in range(2 * i + 1):
                print("*", end="")

            
            print()

    def inverted_pyramid(self, n):
        
        for i in range(n):
           
            for j in range(i):
                print(" ", end="")

            
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")

            
            print()

if __name__ == "__main__":
    N = int(input())

   
    sol = Solution()

    sol.pattern9(N)
