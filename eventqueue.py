__author__ = 'sean'
import exceptions



class EventQueue:
    _q = {}
    def __init__(self):
        self._q = {}
    def push(self, event):
        try:
            self._q[event.y].append(event)
        except exceptions.KeyError:
            self._q[event.y] = [event]
    def remove(self, event):
        try:
            for i in range(len(self._q[event.y])):
                if self._q[event.y][i] == event:
                    self._q[event.y].pop(i)
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
        try:
            return self._q[y].pop()
        except exceptions.KeyError:
            return None
        except exceptions.IndexError:
            return None
    def remove(self, par):
        found = -1
        for i in range(len(self._q[par.y])):
            if self._q[par.y][i].key == par.key:
                found = i
                break
        if found > 0:
            self._q[par.y].pop(found)

    def isEmpty(self):
        for key in self._q.keys():
            if len(self._q[key]) > 0:
                return False
        return True


