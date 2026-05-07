import sys
import math
sys.stdin=open('python code/input.txt', 'r')
sys.stdout=open('python code/output.txt', 'w')


#decue

from collections import deque
dq=deque([1,2,3,4])
dq.append(5) # It will add 5 at the end of the deque
print(dq)

dq.appendleft((7))# It will add 7 at the beginning of the deque
print(dq)

print (dq.pop()) # It will remove the last element of the deque and return it
print(dq)

print(dq.popleft())# It will remove the first element of the deque and return it
print(dq)

dq.extend([8,9,10]) # It will add 8,9,10 at the end of the deque
print(dq)

dq.extendleft(['Yash',8])
print(dq)# It will add 'Yash' and 8 at the beginning of the deque. Note that the order of the elements will be reversed when added to the left side of the deque.



from collections import Counter
arr=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(arr[2])
print(list(arr.elements())) # It will return a list of all the elements in the counter
