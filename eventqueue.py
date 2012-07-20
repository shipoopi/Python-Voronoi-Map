__author__ = 'sean'
import exceptions

class Node:
    event = None
    next = None
    prev = None
    y = 0
    def __init__(self, e):
        self.event = e
        self.y = int(e.y)
        self.Next = None
        self.Prev = None
    def __str__(self):
        return "[Node: y: %d [%s]]" % (self.y, self.event)


class EventQueue:
    first = None
    def __init__(self):
        self.first = None
    def __str__(self):
        output = "["
        current = self.first
        while current:
            output += str(current)+","
            current = current.next
        output += "]";
        return output
    def push(self, event):
        new = Node(event)
        if not self.first:
            self.first = new #insert the first one
            return
        current = self.first
        while current:
            if not current.next or current.next.y >= new.y:
                #found the insertion point
                if current.y <= new.y:
                    #insert after current
                    new = Node(event)
                    new.next = current.next
                    new.prev = current
                    current.next = new
                    return
                else:
                    #insert before current
                    new.prev = current.prev
                    new.next = current
                    if not current.prev:
                        #we have a new first node
                        self.first = new
                    else:
                        current.prev.next = new
                    current.prev = new
                    return
            current = current.next
    def remove(self, event):
        current = self.first
        while current:
            if current.event == event:
                if self.first.event == current.event:
                    self.first = None
                #remove this one from the chain
                current.prev.next = current.next
                current.next.prev = current.prev
                del(current)
            current = current.next
    def pop(self, y):
        inty = None
        if not self.first:
            return None
        if y == None:
            print "pop the first"
            inty = self.first.y
        else:
            inty = int(y)

        current = self.first
        while current:
            print "current: %s" % current
            if current.y == inty:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                #node is removed from chain
                if current == self.first:
                    #set a new first
                    if current.prev:
                        self.first = current.prev
                    else:
                        self.first = current.next
                e = current.event
                del(current) #prevent memory leak
                return e
            current = current.next
        return None
    def getAll(self):
        all = []
        current = self.first
        while current:
            all.append(current.event)
            current = current.next
        return all
    def isEmpty(self):
        if self.first:
            return False
        else:
            return True


