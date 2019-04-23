# batch_file_rename_basename.py
# Created: 4 23 2019

"""
Batch rename a group of files in a given directory about basename not extension
"""

# meta
__author__ = 'ZzLee'
__version__ = '1.0'

import os
import argparse


def batch_rename(work_dir):
    """
    Batch rename a group of files in a given directory,
    about basename not extension
    """
    counter = 1
    for filename in os.listdir(work_dir):
        # Get the file basename
        split_file = os.path.splitext(filename)
        extension = split_file[1]
        # Rename the current file basename
        newname = str(counter) + extension

        # Rename the files
        os.rename(
            os.path.join(work_dir, filename),
            os.path.join(work_dir, newname)
        )
        counter += 1


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    return parser


def main():
    """
    This will be called if the script is directly invoked.
    """
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]

    batch_rename(work_dir)


if __name__ == '__main__':
    main()