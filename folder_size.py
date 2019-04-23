# batch_file_rename_basename.py
# Created: 4 23 2019

"""
This will scan the current directory and all subdirectories and display the size.
"""
"""
what I have learned about this script?
-sys.exit(some_sentence:str)
    exit the program with some sentences

-os.walk(a_dir_name:str)
    return  a tuple(dirpath, dirnames, filenames)
    
    description: 
    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).
"""

# meta
__author__ = 'ZzLee'
__version__ = '1.0'


import os
import sys # for arguments

try:
    directory = sys.argv[1]   # Set the variable directory to be the argument supplied by user.
except IndexError:
    sys.exit("Must provide an argument for directory.")

dir_size = 0    # initial the size to 0
unit_dict = {
    'Bytes': 1,
    'Kilobytes': float(1) / 1024,
    'Megabytes': float(1) / (1024 * 1024),
    'Gigabytes': float(1) / (1024 * 1024 * 1024),
        }
for (path, dirs, files) in os.walk(directory):      # Walk through all the directories. 
    for file in files:                              # Get all the files
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)       # Add the size of each file in the root dir to get the total size.

size_list = [str(round(unit_dict[key] * dir_size, 2)) + " " + key for key in unit_dict] # List of units

if dir_size == 0: 
    print ("File Empty") # Sanity check to eliminate corner-case of empty file.
else:
    for unit in size_list:
        print ("Folder Size: " + unit)