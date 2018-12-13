import time, sys
import threading
#Allows for ... animation
class Threading():
    def __init__(self, stringWaiting, stillThreading):
        self.index = 0
        self.stringWaiting = stringWaiting
        self.stillThreading = stillThreading
        self.x = 0
        self.t = threading.Thread(target=self.waiting)
        self.t.start()
        
    def waiting(self):
        while self.stillThreading == True:
            self.x = self.index % 4
            dots = self.x *'.' + (3-self.x) * ' '
            sys.stdout.write("\r" + self.stringWaiting + dots)
            time.sleep(0.5)
            sys.stdout.flush()
            self.index+=1
        self.stillThreading = True
