#!/usr/bin/env python

def run_state(work_log):
    return False

if __name__ == '__main__':
    import os
    import sys
    import Log
    
    loop_toggle = True
    work_log = ""
    
    while loop_toggle:
        print("Do you want to Open an existing log or Create a new one?")
        answer = sys.stdin.readline().strip()
        if answer == "o":
            print("Which log do you want to open?")
            name = sys.stdin.readline().strip()
            path = os.path.join(os.path.realpath(__file__)[0:-8], "LOGS", name + ".txt")
            if not os.path.isfile(path):
                print path
                print "There is no such log!"
            else:
                work_log = Log.Log(path)
                loop_toggle = run_state(work_log)
        elif answer == "c":
            print("Enter a name for the log: (Optionnal: Use _ to separate the subname)")
            name = sys.stdin.readline().strip()
            temp = name.split("_")
            path = os.path.join(os.path.realpath(__file__)[0:-8], "LOGS", name  + ".txt")
            if len(temp) == 1:
                Log.mk_log_file(path, temp[0])
            else:
                Log.mk_log_file(path, temp[0], temp[1])
        elif answer =="q":
            loop_toggle = False
        
       
    try:
        work_log.save()
    except BaseException:
        print("Could not save the log.")
        
