#example of multi threading and without multi threading
#ex:with out multi threading

import time
def double(numbers):
    for n in numbers:
        time.sleep(3)
        print('double values:',2*n)

def square(numbers):
    for n in numbers:
        time.sleep(3)
        print('square values:',n*n)
numbers=[1,2,3,4,5]
begintime=time.time()
double(numbers)
square(numbers)
endtime=time.time()
print('the total time taken:',endtime-begintime)

