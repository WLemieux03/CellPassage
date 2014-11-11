#!/usr/bin/env python
from datetime import datetime
import re

class Passage:
    culture_start = 1
    yielded = 0
    plated = 0
    p_num = 0
    time = datetime.now()
    
    def __init__(self, start, yielded, plated, p_num, time):
        self.culture_start = start
        self.yielded = yielded
        self.plated = plated
        self.p_num = p_num
        self.time = time
        return
    
    def to_str(self):
        return str(self.culture_start) + " , " + str(self.yielded) + " , " + str(self.plated) + " , " + str(self.p_num) + " , " + str(self.time)
        
def cPD(P1, P0):
    import math
    return (math.log10(P1.yielded)-math.log10(P0.plated))/math.log10(2)

def DT(P1, P0):
    dTime = P1.time-P0.time
    return (int(dTime.total_seconds())/3600)/cPD(P1, P0)