__author__ = 'sean'

class VQueue:
    def __init__(self):
        self.q = []
        self.i = 0
    def enqueue(self, p):
        self.q.append(p)
    def dequeue(self):
        self.sort()
        return self.q.pop()
    def sort(self):
        try:
            import operator
        except ImportError:
            keyfun = lambda e: e.y
        else:
            keyfun = operator.attrgetter("y")
        #TODO:  need to check if we need a reverse=True flag in the sort
        self.q.sort(key=keyfun)
    #TODO:  the rest of the class