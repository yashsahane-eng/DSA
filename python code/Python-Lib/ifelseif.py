import sys

sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')



class Solution:
  def student_grade(self,marks):
    if marks>=90:
      print("Grade A")
    elif marks >=70:
      print("Grade B")
    elif marks >=50:
      print("Grade C")
    elif marks >=35:
      print("Grade D")
    else:
      print("Fail")

if __name__ == "__main__":

  solution=Solution()

  marks=int(input("Enter the marks of the student: "))
  solution.student_grade(marks)
