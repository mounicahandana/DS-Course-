'''

THREADING 

In process there r lot of threads each thread runs one after another 

mainly we use start(),sleep() and join()

'''

from time import sleep
from threading import *
import threading
class FUN(Thread):
    def func(self):
        for i in range(3):
            print('hi i m thread 1')
            print(threading.current_thread().getName())
            sleep(2)

class FUN2(Thread):
    def func2(self):
        for i in range(3):
            print('HI I AM THREAD 2')
            print(threading.current_thread().getName())

a=FUN()
b=FUN2()
a.start()
sleep(2)
a.func()
b.func2()
