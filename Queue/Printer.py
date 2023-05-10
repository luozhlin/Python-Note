class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # The print rate
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):
        """
        The tick method decrements the internal timer and sets the printer to idle if the task is completed.
        """
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining-1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        """
        Judge if the printer is busy
        """
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self, newtask):
        """
        Calculate the seconds to finish new taks. Since page rate is base on minutes, we need first change it into seconds.
        """
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

import random
import numpy as np

class Tasks:
    def __init__(self, time, pages_range):
        self.timestamp = time
        self.pages = random.randrange(1,pages_range)

    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    
from pythonds.basic.queue import Queue

def simulation(numSeconds, pagesPerMinute, pages_range, num_student):

    labprinter = Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask(num_student):
            task = Tasks(currentSecond, pages_range)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask= printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()  # printer work time + 1s

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask(num_student):
    prob_taks_per_second  = np.floor(1800 / num_student)  # Consider the reciprocal of the time of 1 task, sugget use floor becasue the prob of 1 second to create a task can cover the reality. Otherwise,  you will use less time to create a task
    num = random.randrange(1, prob_taks_per_second+1)
    if num == prob_taks_per_second:
        return True
    else:
        return False
    
for i in range(10):
    simulation(3600,5,10,20)

# Modify: Suppose the number of students is x and print pages is y. Still, each students has up to tasks.




