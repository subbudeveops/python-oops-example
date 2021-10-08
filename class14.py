#garbage collection
# and Destructor
import time
class Test:
    def __init__(self):
        print('object initilizing')
    
    def __del__(self):
        print('filfuling activites doing clesnup activites')

t=Test()
t=None