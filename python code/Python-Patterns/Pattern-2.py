import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
    
 
    def pattern2(self, n):
        
        
        for i in range(n):
            
            
            for j in range(i+1):
                print("*", end="")
                
        
            print()

    def main(self):
        N = int(input())

        
        sol = Solution()

        sol.pattern2(N)

if __name__ == "__main__":
    Solution().main()