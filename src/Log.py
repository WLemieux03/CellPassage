#!/usr/bin/env python
import datetime

class Log:
    name = ""
    alt_name = ""
    cell_list = {}
    
    def __init__(self, path):
        import re
        import CLine
        
        log_file = open(path, 'r')
        temp = []
        for line in log_file:
            temp.append(line)
        log_file.close()
        
        l=len(temp)
        for line in range(0, l-1):
            if "name : " in temp[line]:
                self.name = temp[line][7:-1]
            elif "alt_name : " in temp[line]:
                self.alt_name = temp[line][11:-1]
            elif "CLine ; " in temp[line]:
                m = re.search("CLine ; (?P<ID>\w+) ; (?P<name>\w+) ; (?P<NoL>[.\d]) :")
                temp_passage = []
                for i in range(line+1, line+int(m.group("NoL"))):
                    temp_passage.append(temp[i])
                self.cell_list[m.group("ID")] = CLine(m.group("ID"), m.group("name"))
                self.cell_list[m.group("ID")].str_passage(temp_passage)
        return

    def add_line(self, line_name, PDi, plated, time=datetime.datetime.now()):
        ID = new_ID()
        self.cell_list[ID] = (Passage(ID, line_name))
        self.cell_list[ID].mk_passage(1, PDi, plated, 0, time)
        return ID
    
    def mk_passage(self, ID, culture_start, yielded, plated, p_num, time):
        self.cell_list[ID].mk_passage(1, PDi, plated, 0, time)
        return ID
    
    def close(self, ID):
        self.cell_list[ID].set_not_culture()
        return ID
    
    def save(self):
        import os
        if self.alt_name == "":
            path = os.path.join(os.path.realpath(__file__)[0:-7], "LOGS", self.name + ".txt")
        else:
            path = os.path.join(os.path.realpath(__file__)[0:-7], "LOGS", self.name + "_" + self.alt_name + ".txt")
        print path
        temp = open(path, "w+")
        temp.write("name : " + self.name+"\n")
        temp.write("alt_name : " + self.alt_name+"\n")
        print self.cell_list
        for line in self.cell_list:
            temp.write("CLine ; " + line.ID + " ; " + line.cell_line_name + " ; " + len(line.passage_list) + " :\n")
            for passage in line.passage_list:
                temp.write("passage"+"\n")
        temp.close()
    
    def in_culture(self):
        temp = []
        for ID in cell_list.keys():
            if cell_list[ID].in_culture:
                temp.append(ID)
        return temp
    
def mk_log_file(path, name, alt_name = ""):
    log_file = open(path, 'w+')
    
    log_file.write("name : "+name+"\n")
    log_file.write("alt_name : "+alt_name+"\n")
    log_file.close()
    return path