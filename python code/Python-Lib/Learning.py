import sys
import math
sys.stdin=open('python code/input.txt', 'r')
sys.stdout=open('python code/output.txt', 'w')


fruit_list=['apple' , 'pineapple' , 'kiwi']
print(sorted(fruit_list ,reverse=True , key=len))

arr=[6,5,4,3,2,2,2,1]

print(math.prod(arr))
print(min(arr))
print(max(arr))
print(sum(arr))

arr2=[True , False , True , False , True]
print(any(arr2)) # Any One is True

print(all(arr2))# All should be True   

print(arr.count(2)) # Count the number of 2's in the list

arr3=[1,2,3,4,5]
print(list(enumerate(arr3))) # It will give the index and the value of the list in the form of tuple

print(list(reversed(arr3))) # It will reverse the list

arr4=list(range(2,15,2))
print(arr4)