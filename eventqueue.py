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
    def pop(self, y):
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


