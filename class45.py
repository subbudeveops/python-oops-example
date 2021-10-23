#join() method: if a Thread want to wait until completing some other thread then we should go for join() methdo
#ex:
from threading import *
import time
def display():
    for n in range(5):
        print('seetha thread')
        time.sleep(3)
t=Thread(target=display)
t.start()
t.join()
#t.join(5)#exactly 10sec is waiting main thread
for n in range(5):
    print('rama thread')