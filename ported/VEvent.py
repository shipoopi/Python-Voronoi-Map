__author__ = 'sean'

import random

class VEvent:
    def __init__(self, p, pe):
        self.point = p
        self.pe = pe
        self.y = p.y
        self.key = random.random() * 100000000
        self.arch = None
        self.value = 0
    def compare(self, other):
        #TODO:  need to check if this works
        if(self.y > other.y):
            return True
        else:
            return False