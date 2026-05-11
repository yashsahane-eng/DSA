import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
    
    
    def pattern6(self, n):
        
        
        for i in range(0,n):
            
            
            for j in range(0,n-i):
                print(j+1, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = int(input())

        
        sol = Solution()

        sol.pattern6(N)

if __name__ == "__main__":
    Solution().main()
