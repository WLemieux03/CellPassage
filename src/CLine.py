#!/usr/bin/env python

class CLine:
    ID = "M0001"
    cell_line_name = ""
    passage_list = []
    in_culture = True
    
    def __init__(self, ID, cell_line_name, temp_passage):
        self.ID = ID
        self.cell_line_name = cell_line_name
        return
    
    def current_PD(self):
        PD = passage_list[0].yielded
        for i in range(1, len(passage_list)-1):
            PD += Passage.cPD(passage_list[i], passage_list[i-1])
        return PD
    
    def DT_av(self):
        DT_list = []
        for i in range(len(passage_list)-1, 1, -1):
            DT_list.append(Passage.DT(self.passage_list[i], self.passage_list[i-1]))
        i = 2
        DT_sum = 0
        for DT in DT_list:
            DT_sum += DT/i
            i *= 2
        DT_av = DT_sum/(1-1/i)
        return DT_av
    
    def dDT_av(self):
        DT_list = []
        dDT_list = []
        for i in range(len(passage_list)-1, 1, -1):
            DT_list.append(Passage.DT(self.passage_list[i], self.passage_list[i-1]))
        for j in range(1, len(DT_list)-1):
            dDT_list.append(DT_list[j]-DT_list[j-1])
        i = 2
        dDT_sum = 0
        for dDT in dDT_list:
            dDT_sum += DT/i
            i *= 2
        dDT_av = dDT_sum/(1-1/i)
        return dDT_av
    
    def get_cell_num(self, target):
        time = target-self.passage_list[-1].time
        h_time = int(time.total_seconds())/3600
        final = self.passage_list[-1].plated*2^(h_time/(self.DT_av()+self.dDT_av))
        return final
    
    def mk_passage(self, culture_start, yielded, plated, p_num, time):
        self.passage_list.append(Passage(culture_start, yielded, plated, p_num, time))
        return
    
    def str_passage(self, temp_passage):
        for line in temp_passage:
            str_list = string.split(" , ")
            culture_start = str_list[0]
            yielded = str_list[1]
            plated = str_list[2]
            p_num = str_list[3]
            day_time = re.findall(r"\d+", str_list[4])
            time = datetime(int(day_time[0]), int(day_time[1]), int(day_time[2]), int(day_time[3]), (int(day_time[4])/15)*15)
            passage_list.append(Passage(culture_start, yielded, plated, p_num, time))
        return
    
    def not_cultured(self):
        self.in_culture = False
        return self.ID
    