# Multithreading
# import threading, Threading is built in module, multiple thread can run concurrently
# threading is lightweight process
# All threads in python shares same memory space.
import threading
from time import sleep
def f1():
    for i in range(3):
        print(i)
        sleep(1)
def f2():
    for j in range(3):
        print(j)
        sleep(2)
# f1()
# f2()
t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
t2.start()
t1.join()
t2.join()