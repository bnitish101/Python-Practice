from time import sleep
from threading import *


class Hello(Thread):  # it imports form threading module
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)  # it imports form time module


class Hi(Thread):  # it imports form threading module
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)  # it imports form time module


t1 = Hello()
t2 = Hi()

Hello.start(t1)  # first thread: instead of "Hello.run(t1)" we use "start()" which indirectly calls "run()"
sleep(0.2)  # it imports form time module
t2.start()  # second thread: instead of "t2.run()" we use "start()" which is indirectly call "run()"

t1.join()  # join() method means, first thread will wait for main thread
t2.join()  # join() method means, second thread will wait for main thread
print('Bye')  # main thread: as we know every execution done by main thread
