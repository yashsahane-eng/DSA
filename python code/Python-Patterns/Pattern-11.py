import sys
sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')
class Solution:
    
    def pattern11(self, n):
        
        start = 1

        
        for i in range(n):

           
            if i % 2 == 0:
                start = 1

            
            else:
                start = 0

            
            for j in range(i + 1):
                print(start, end="")
                if j != i:
                    print(" ", end="")

                start = 1 - start

            
            print()


if __name__ == "__main__":
    N = int(input())

    
    sol = Solution()

    sol.pattern11(N)