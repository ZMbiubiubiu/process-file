# batch_file_rename_basename.py
# Created: 4 23 2019

"""
Create a simple stopwatch application using Python's time module.

"""
# meta
__author__ = 'ZzLee'
__version__ = '1.0'

"""
what I have learned about this script?
-print(end="\r")
    Loop printing, and overwrite(循环打印, 不换行而是覆盖上一次打印的结果)

-KeyboardInterrupt
    捕捉 Ctrl + C
"""

import time

print('Press ENTER to begin, Press Ctrl + C to stop')
try:
    input() # For ENTER. 
    starttime = time.time()
    print('Started')
    while True:
        print('Time Elapsed: ', round(time.time() - starttime, 0), 'secs', end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print('Stopped')
    endtime = time.time()
    print('Total Time:', round(endtime - starttime, 2),'secs')