# batch_file_rename_basename.py
# Created: 4 23 2019

"""
This script will search for all *.txt files in the given directory, 
zip them using the program you specify and then date stamp them

"""
# meta
__author__ = 'ZzLee'
__version__ = '1.0'

"""
what I have learned about this script?
-time.strftime
    strftime(format[, tuple]) -> string
    
    Convert a time tuple to a string according to a format specification.
"""



import os                   
from time import strftime   # Load just the strftime Module from Time

logsdir = "/home/bingo/Test"      # Set the Variable logsdir
zip_program = "tar -cvf"       # c(create) v(view) f(+file)

os.chdir(logsdir)             # Change directory to the logsdir

for file in os.listdir(logsdir):                         # Find all the files in the directory
    if file.endswith(".txt"): 
        basename = os.path.splitext(file)[0]                         # get the basename of the file (excluding the extension)
        zip_file = basename + "_" + strftime("%Y-%m-%d") + ".zip"    # Create the Variable zip_file, this is the file in the directory, then we add a suffix with the date and the zip extension
        os.system(zip_program + " " +  zip_file +" "+ file)      # tar the txts into dated zip file for each server.
        os.remove(file)                                        # Remove the original txt files
