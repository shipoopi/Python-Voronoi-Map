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
        if not y:
            #pick the first
            if len(self._q) == 0:
                return None
            try:
                for key in self._q.keys():
                    return self._q[key].pop()
                return None
            except exceptions.KeyError:
                return None
            except exceoptions.IndexError:
                return None
        try:
            return self._q[y].pop()
        except exceptions.KeyError:
            return None
        except exceptions.IndexError:
            return None
    def isEmpty(self):
        for key in self._q.keys():
            if len(self._q[key]) > 0:
                return False
        return True


