#how can set my own name for thread
# setting and getting name of thread
from threading import *
print(current_thread().getName())

current_thread().setName('subbu')
#or
current_thread().name='bhavani'

print(current_thread().getName())
#or
print(current_thread().name)
print()
#very thread internaly unique identification number by using implict variable 'ident'
from threading import *
def test():
    print('child thread')
t=Thread(target=test)
t.start()
print('main thread identification number:',current_thread().ident)
print('child thread identification number:',t.ident)
