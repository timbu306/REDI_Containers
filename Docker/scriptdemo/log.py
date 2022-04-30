import time



with open("mylogs.log", "r") as logfile:
        for line in logfile.readlines():
                n = line
                print (n)
                time.sleep(1)