#Effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated.
#multiprocessing supports two types of communication channel between processes:

#1.Queue
#2.Pipe
#Queue : A simple way to communicate between process with multiprocessing is to use a Queue to pass messages back and forth. Any Python object can pass through a Queue.
#Note: The multiprocessing.Queue class is a near clone of queue.Queue.
#Consider the example program given below:
import multiprocessing
def square_list(mylist,q):
    for num in mylist:
        q.put(num* num)
def display(q):
    print("Queae element")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")   
if __name__ == "__main__":
    # input list
    mylist = [1,2,3,4] 
    q = multiprocessing.Queue()
  
    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p2 = multiprocessing.Process(target=display, args=(q,))
  
    # running process p1 to square list
    p1.start()
    p1.join()
  
    # running process p2 to get queue elements
    p2.start()
    p2.join()
