import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
    
   
    def pattern5(self, n):
        
       
        for i in range(0,n):
            
            
            for j in range(0,n-i):
                print("*", end="")
                
            
            print()

    def main(self):
        N = int(input())

       
        sol = Solution()

        sol.pattern5(N)

if __name__ == "__main__":
    Solution().main()
