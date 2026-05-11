import sys

sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:
  def which_week_day(self,day):
    if day<1 or day>7:
      print("Invalid input")
      return
    
    match day:
      case 1:
        print("Monday")
      case 2:
        print("Tuesday")
      case 3:
        print("Wednesday")
      case 4:
        print("Thursday")
      case 5:
        print("Friday")
      case 6:
        print("Saturday")
      case 7:
        print("Sunday")

if __name__ == "__main__":
  Solution=Solution()
  day=int(input("Enter the day number (1-7): "))
  Solution.which_week_day(day)
   