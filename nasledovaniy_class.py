import time

class Loggable:
    def log(self,msg):
        print(str(time.ctime()) + ": "+ str(msg))

class LoggableList(list,Loggable):
    def append(self,msg):
        super(LoggableList, self).append(msg)
        Loggable.log(self,msg)


x = LoggableList()
x.append('r')


