__author__ = 'sean'
import exceptions

class Node:
    event = None
    y = 0
    def __init__(self, e):
        self.event = e
        self.y = int(event.y)


class EventQueue:
    _q = {}
    def __init__(self):
        self._q = {}
    def push(self, event):
        loc = int(event.y)
        try:
            self._q[loc].append(event)
        except exceptions.KeyError:
            self._q[loc] = [event]
    def remove(self, event):
        loc = int(event.y)
        try:
            for i in range(len(self._q[loc])):
                if self._q[loc][i] == event:
                    self._q[loc].pop(i)
        except exceptions.KeyError:
            return None
        except exceptions.IndexError:
            return None
    def pop(self, y):

        print "queue: %s" % self._q
        if not y:
            #pick the first
            if len(self._q) == 0:
                print "queue is empty, can't pop"
                return None
            try:
                for key in self._q.keys():
                    if len(self._q[key]) > 0:
                        return self._q[key].pop()
                return None
            except exceptions.KeyError as e:
                print "key error"
                return None
            except exceptions.IndexError as e:
                print "index error (%d): %s" % (key, str(e))
                return None
        loc = int(y)
        try:
            return self._q[loc].pop()
        except exceptions.KeyError:
            return None
        except exceptions.IndexError:
            return None
    def remove(self, par):
        loc = int(par.y)
        found = -1
        for i in range(len(self._q[loc])):
            if self._q[loc][i].key == par.key:
                found = i
                break
        if found > 0:
            self._q[loc].pop(found)

    def isEmpty(self):
        for key in self._q.keys():
            if len(self._q[key]) > 0:
                return False
        return True


