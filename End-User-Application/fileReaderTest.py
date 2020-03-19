import csv
import time
with open("testFile.txt", 'r', encoding='utf-8-sig') as thefile:
    thefile.seek(0,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if line:
            print(line)
        if not line:
            time.sleep(0.03) # Sleep briefly
            continue
