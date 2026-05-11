import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
    
   
    def pattern3(self, n):
        
       
        for i in range(1,n+1):
            
            
            for j in range(1,i+1):
                print(j, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = int(input())

        
        sol = Solution()

        sol.pattern3(N)

if __name__ == "__main__":
    Solution().main()
