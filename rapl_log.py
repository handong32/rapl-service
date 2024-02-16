
import subprocess
from subprocess import Popen, PIPE, call
import time
import sys
import os
import signal

f = open("/tmp/rapl.log", "w")
run = True
def handler_stop_signals(signum, frame):
    global run
    run = False
    ## make sure to close file
    if not f.closed:
        f.close()

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

def runLocalCommandGet(com):
    p1 = Popen(list(filter(None, com.strip().split(' '))), stdout=PIPE)
    return p1.communicate()[0].strip()

output = 0.0

try:
    ## run forever?
    while run:        
        output = runLocalCommandGet("tmpdir/uarch-configure/rapl-read/raplog -m")
        values = output.decode('utf-8').split(',')
        cpupkg = float(values[0])
        drampkg = float(values[1])
        
        ## check if energy value is valid
        if cpupkg > 0.0 and cpupkg < 1000.0:
            f.write(f"{cpupkg} {drampkg}\n")
            f.flush()
        else:
            time.sleep(1)
except Exception as e:
    run = False
    print(e)
    ## make sure to close file
    if not f.closed:
        f.close()
