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
    def remove(self, e):
        index = -1
        self.i = 0
        while self.i < len(self.q):
            if self.q[self.i] == e:
                index = self.i
                break
            self.i += 1
        #TODO:  don't know if this will work
        self.q.pop(self.i)
    def isEmpty(self):
        return len(self.q) == 0
    def clear(self):
        self.q = []