# batch_file_rename_basename.py
# Created: 4 23 2019

"""
This script will search for all *.txt files in the given directory, 
zip them using the program you specify and then date stamp them

"""
# meta
__author__ = 'ZzLee'
__version__ = '1.0'



import os                   
from time import strftime   # Load just the strftime Module from Time

logsdir = "/home/bingo/Test"      # Set the Variable logsdir
unzip_program = "tar -xvf"       # x v(view) f(+file)

os.chdir(logsdir)             # Change directory to the logsdir

for file in os.listdir(logsdir):                    # Find all the zip files in the directory
    if file.endswith(".zip"): 
        os.system(unzip_program + " " +  file)      # untar the zips into original file for each server.
        os.remove(file)                             # Remove the zip files
