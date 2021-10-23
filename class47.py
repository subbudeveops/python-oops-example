#main advantage of Daemon Thread:When last non-Daemon thread treminates automatically all daemon threads will be terminated we are not rerequired to terminated explicitly
#ex: car game
#background scenaries-----daemon
#ex:cinema shooting
#hero,heroin-----non daemon
#makeupman------daemon
#ex:
from threading import *
import time
def job():
    for i in range(10):
        print('lazy thread')
        time.sleep(2)
t=Thread(target=job)
t.setDaemon(True)
t.start()
time.sleep(10)
print('end main thread')


#supporting job can be implemented Daemon threads
#where main job should be implemented by non daemon threads