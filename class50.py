#communication beetween processes
import threading
import multiprocessing
result=[]
def square_list(mylist):
    global result
    for num in mylist:
        result.append(num*num)
    print('Result(In procees):{}'.format(result))
if __name__=="__main__":
    mylist=[1,2,3,4,5]
    t=multiprocessing.Process(target=square_list,args=(mylist,))
    t.start()
    t.join()
    print("Result(in main program): {}".format(result))