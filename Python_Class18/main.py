import threading
import os
import time
  
def task1():
    time.sleep(2)
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
  
def task2():
    time.sleep(2)
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
  
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
  
    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)  
  
    # starting threads
    t1.start()
    t2.start()
  
    # wait until all threads finish
    t1.join()
    t2.join()


import multiprocessing
import time
import math

result_1 = [] #1, 4, 9, 16
result_2 = [] #1, 8, 27, 64
result_3 = []

def calculation_a(numbers):
    time.sleep(2)
    for number in numbers:
        result_1.append(math.sqrt(number**2))

def calculation_b(numbers):
    time.sleep(2)
    for number in numbers:
        result_2.append(math.sqrt(number**3))

def calculation_c(numbers):
    time.sleep(2)
    for number in numbers:
        result_3.append(math.sqrt(number**4))

if __name__ == '__main__':

    numberList = list(range(100))

########### method calls with multiprocessing ###########

    process_1 =  multiprocessing.Process(target=calculation_a, args=(numberList,))
    process_2 =  multiprocessing.Process(target=calculation_b, args=(numberList,))
    process_3 =  multiprocessing.Process(target=calculation_c, args=(numberList,))

    start = time.time()
    process_1.start()
    process_2.start()
    process_3.start()
    end = time.time()
    print(end-start)


########### normal method calls ###########
    start = time.time()
    calculation_a(numberList)
    calculation_b(numberList)
    calculation_c(numberList)
    end = time.time()

    print(end-start)

