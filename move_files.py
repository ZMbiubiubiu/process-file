# move_files.py
# Created: 4 24 2019
# meta
__author__ = 'ZzLee'
__version__ = '1.0'
"""
Description   : This will move all the files from the src directory that are over 
x days old to the destination directory.
"""

"""
what I have learned about this script?
-parser.add_argument(..., default=:str/int/etc, ... , require=:bool)
"""

import argparse
import shutil
import sys
import time
import os

usage = 'python move_files_over_x_days.py -src [SRC] -dst [DST] -days [DAYS]'
description = 'Move files from src to dst if they are older than a certain number of days.  Default is 240 days'

parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument('-src', '--src', type=str, nargs='?', default='.', help='(OPTIONAL) Directory where files will be moved from. Defaults to current directory')
parser.add_argument('-dst', '--dst', type=str, nargs='?', required=True, help='(REQUIRED) Directory where files will be moved to.')
parser.add_argument('-days', '--days', type=int, nargs='?', default=240, help='(OPTIONAL) Days value specifies the minimum age of files to be moved. Default is 240.')
args = parser.parse_args()

if args.days < 0:
	args.days = 0

# Get the arguments supplied by user
src = args.src  # Set the source directory
dst = args.dst  # Set the destination directory
days = args.days #Set the number of days

now = time.time()  # Get the current time

if not os.path.exists(dst): # If dst not exists then create it.
	os.mkdir(dst)

for f in os.listdir(src):       # Loop through all the files in the source directory
    f = os.path.join(src, f)    # Full name the f file
    if os.stat(f).st_mtime < now - days * 86400:  # Work out how old they are, if they are older than 240 days old
        if os.path.isfile(f):  # Check it's a file
            shutil.move(f, dst)  # Move the files