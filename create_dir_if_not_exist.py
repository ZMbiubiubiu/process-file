# create_dir_if_not_exist.py
# Created: 4 23 2019

"""
Checks to see if a directory exists in the users home
directory, if not then create it
"""

# meta
__author__ = "ZzLee"
__version__ = "1.0"

import os

MESSAGE = "The directory already exists"
TESTDIR = "Test"

def create_dir_if_not_exist():
    try:
        home = os.path.expanduser("~")
        # make a full path safely
        full_name = os.path.join(home, TESTDIR)
        if not os.path.exists(full_name):
            os.makedirs(full_name)
        else:
            print(MESSAGE)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_dir_if_not_exist()