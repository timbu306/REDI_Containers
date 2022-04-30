import time

with open("mylogs2.log", "r") as logfile:
        for line in logfile.readlines():
                n = line
                print (n)
                time.sleep(1)